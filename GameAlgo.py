import json
import math
from client import Client
from Classes import Pokemon
from Classes import Agent
from Ex3Files import DiGraph
from Ex3Files import Node
from Ex3Files import GraphAlgo
from Ex3Files.PPQ import *

Epsilon = 0.00000001


class GameAlgo:

    def _init_(self):
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

    def init_pokemons(self, pokemons):
        pokemon_obj = json.loads(pokemons)
        for p in pokemon_obj['Pokemons']:
            print(p)
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
            print(a)
            temp = Agent.Agent(a['Agent'])
            self.agents[temp.id] = temp

    def find_pok_src_dst(self, pokemon: Pokemon):
        # Finding on which edge the pokemon is and update the pokemon values
        for node1 in self.graph.get_graph().nodes.values():
            for node2 in self.graph.get_graph().nodes.values():
                nodeDist = GameAlgo.find_dist_nodes(self, node1, node2)
                PokeDist = pokemon[2].dist_pokemon_node(node1) + pokemon[2].dist_pokemon_node(node2)
                # if the distances is almost equals
                if abs(nodeDist - PokeDist) <= Epsilon:
                    print(node1)
                    print(node2)
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


def main():
    PORT = 6666
    # server host (default localhost 127.0.0.1)
    HOST = '127.0.0.1'
    MyClient = Client()
    MyClient.start_connection(HOST, PORT)
    MyClient.add_agent("{\"id\":0}")
    MyClient.add_agent("{\"id\":1}")
    MyClient.add_agent("{\"id\":2}")
    MyClient.add_agent("{\"id\":3}")
    # MyClient.start()

    game = GameAlgo()
    # game.init_pokemons(MyClient.get_pokemons())
    # game.init_graph(MyClient.get_graph())
    print(MyClient.get_agents())
    game.update_game(MyClient.get_pokemons(), MyClient.get_agents(), MyClient.get_graph())
    game.all_pok_src_dst()
    # game.init_agents(MyClient.get_agents())
    print(game.pokemons)
    print("Hello")


if _name_ == "_main_":
    main()
