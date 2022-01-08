import json
import math
import sys

from client import Client
from Classes import Agent
from Ex3Files import DiGraph
from Ex3Files import Node
from Ex3Files import GraphAlgo
from Classes.PPQ import *

Epsilon = 0.00000001


class GameAlgo:

    def __init__(self):
        self.graph = GraphAlgo.GraphAlgo()
        self.pokemons = PQByPokemon()
        self.agents = dict()

    def update_game(self, pokemons=None, agents=None, graph=None):
        if pokemons != None:
            self.init_pokemons(pokemons)
        if agents != None:
            self.init_agents(agents)
        if graph != None:
            self.init_graph(graph)
        self.all_pok_src_dst()

    def init_pokemons(self, pokemons):
        self.pokemons.reset()
        pokemon_obj = json.loads(pokemons)
        for p in pokemon_obj['Pokemons']:
            temp = Pokemon.Pokemon(p['Pokemon'])
            self.pokemons.add(temp)

    def init_graph(self, graph):
        graphObj = json.loads(graph)
        myGraph = GraphAlgo.GraphAlgo()
        myGraph.load_from_json(graphObj)
        self.graph = myGraph

    def init_agents(self, agents):
        agentsObj = json.loads(agents)
        for a in agentsObj['Agents']:
            temp = Agent.Agent(a['Agent'])
            self.agents[temp.id] = temp

    def allocate_all_agents(self):
        for a in self.agents.values():
            if a.next_pokemon == None:
                # self.choose_agent()
                self.value_per_time(a)

    def choose_agent(self):
        currPoke = self.pokemons.pop()
        minDist = sys.float_info.max
        choosenAgent = -1
        for a in self.agents.values():
            if a.next_pokemon == None:
                tempDist = self.time_to_poke(a.id, currPoke.src)
                if tempDist < minDist:
                    minDist = tempDist
                    choosenAgent = a.id
            if choosenAgent != -1:
                self.agents.get(choosenAgent).path = \
                self.graph.shortest_path(self.agents.get(choosenAgent).src, currPoke.src)[1]
                self.agents.get(choosenAgent).path.append(currPoke.dst)
                self.agents.get(choosenAgent).path.pop(0)
                self.agents.get(choosenAgent).next_pokemon = 1
                return choosenAgent
        return None

    def time_to_poke(self, agent_id: int, poke_src: int) -> float:
        agent = self.agents.get(agent_id)
        dist = self.graph.shortest_path(agent.src, poke_src)[0]
        return dist / agent.speed

    def find_pok_src_dst(self, pokemon: Pokemon):
        # Finding on which edge the pokemon is and update the pokemon values
        for node1 in self.graph.get_graph().nodes.values():
            for node2 in self.graph.get_graph().nodes.values():
                nodeDist = GameAlgo.find_dist_nodes(self, node1, node2)
                PokeDist = pokemon[2].dist_pokemon_node(node1) + pokemon[2].dist_pokemon_node(node2)
                # if the distances is almost equals
                if abs(nodeDist - PokeDist) <= Epsilon:
                    # check the type in order to decide which one is SRC and which one is DST
                    if pokemon[2].type == 1:  # DST  > SRC
                        src = min(int(node1.id), int(node2.id))
                        dst = max(int(node1.id), int(node2.id))
                    else:
                        src = max(int(node1.id), int(node2.id))
                        dst = min(int(node1.id), int(node2.id))
                    # check if there is a edge between SRC and DST is so update pokemon values
                    if DiGraph.st_edge(src, dst) in self.graph.get_graph().edges:
                        pokemon[2].src = src
                        pokemon[2].dst = dst
                        return

    def find_dist_nodes(self, node1: Node, node2: Node):
        # Same formula to find dist between 2 nodes
        delta_x = pow(node1.pos[0] - node2.pos[0], 2)
        delta_y = pow(node1.pos[1] - node2.pos[1], 2)
        return math.sqrt(delta_x + delta_y)

    def all_pok_src_dst(self):
        for pokemon in self.pokemons.Q:
            if pokemon[2].src is None and pokemon[2].dst is None:
                GameAlgo.find_pok_src_dst(self, pokemon)

    def CMD(self, Client: Client):
        for a in self.agents.values():
            if a.dst == -1:
                if a.path:
                    Client.choose_next_edge('{"agent_id":' + str(a.id) + ', "next_node_id":' + str(a.path.pop(0)) + '}')
                    if not a.path:
                        a.next_pokemon = None

    def begining_of_the_game(self, Client: Client):
        self.init_pokemons(Client.get_pokemons())
        self.init_graph(Client.get_graph())
        self.all_pok_src_dst()
        bla = Client.get_info()
        blaObj = json.loads(bla)
        for i in range(0, int(blaObj['GameServer']['agents'])):
            Client.add_agent('{\"id\":' + str(str(self.pokemons.pop().src)) + '}')

    def game_algorithm(self, Client: Client):
        self.allocate_all_agents()
        self.CMD(Client)
        Client.move()

    def value_per_time(self, a: Agent):
        max_value_per_time = 0
        choosen_poke = None
        for p in self.pokemons.Q:
            if not p[2].is_aget_allocated:
                temp_value = p[2].value / (self.time_to_poke(a.id, p[2].src) + 0.00001)
                if temp_value > max_value_per_time:
                    max_value_per_time = temp_value
                    choosen_poke = p
        choosen_poke[2].is_aget_allocated = True
        a.path = self.graph.shortest_path(a.src, choosen_poke[2].src)[1]
        a.path.append(choosen_poke[2].dst)
        a.path.pop(0)
        a.next_pokemon = 1
