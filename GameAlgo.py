import json
import math
import sys
import time

from client import Client
from Classes.Pokemon import *
from Classes import Agent
from Ex3Files import DiGraph
from Ex3Files import Node
from Ex3Files import GraphAlgo
from Classes.PQ_by_pokemon import *

Epsilon = 0.00000001


def find_dist_nodes(node1: Node, node2: Node):
    # Same formula to find dist between 2 nodes
    delta_x = pow(node1.pos[0] - node2.pos[0], 2)
    delta_y = pow(node1.pos[1] - node2.pos[1], 2)
    return math.sqrt(delta_x + delta_y)


class GameAlgo:

    def __init__(self):
        self.graph = GraphAlgo.GraphAlgo()
        self.pokemons = PQByPokemon()
        self.agents = dict()

    def update_game(self, pokemons=None, agents=None, graph=None):
        if pokemons is not None:
            self.init_pokemons(pokemons)
        if agents is not None:
            self.init_agents(agents)
        if graph is not None:
            self.init_graph(graph)
        self.all_poke_src_dst()

    def init_pokemons(self, pokemons):
        pokemon_obj = json.loads(pokemons)
        for p in pokemon_obj['Pokemons']:
            temp = Pokemon.Pokemon(p['Pokemon'])
            self.pokemons.add(temp)

    def init_graph(self, graph):
        graph_obj = json.loads(graph)
        my_graph = GraphAlgo.GraphAlgo()
        my_graph.load_from_json(graph_obj)
        self.graph = my_graph

    def init_agents(self, agents):
        agents_obj = json.loads(agents)
        for a in agents_obj['Agents']:
            temp = Agent.Agent(a['Agent'])
            self.agents[temp.id] = temp

    def allocate_all_agents(self):
        for a in self.agents.values():
            if a.next_pokemon is None:
                self.choose_agent()

    def choose_agent(self):
        curr_poke = self.pokemons.pop()
        min_dist = sys.float_info.max
        chosen_agent = -1
        for a in self.agents.values():
            if a.next_pokemon is None:
                temp_dist = self.time_to_poke(a.id, curr_poke.src)
                if temp_dist < min_dist:
                    min_dist = temp_dist
                    chosen_agent = a.id
        self.agents.get(chosen_agent).path = self.graph.shortest_path(self.agents.get(chosen_agent).src, curr_poke.src)[
            1]
        self.agents.get(chosen_agent).path.append(curr_poke.dst)
        self.agents.get(chosen_agent).path.pop(0)
        self.agents.get(chosen_agent).next_pokemon = 1
        if chosen_agent != -1:
            return chosen_agent
        return None

    def time_to_poke(self, agent_id: int, poke_src: int) -> float:
        agent = self.agents.get(agent_id)
        dist = self.graph.shortest_path(agent.src, poke_src)[0]
        return dist / agent.speed

    def find_poke_src_dst(self, pokemon: Pokemon):
        # Finding on which edge the pokemon is and update the pokemon values
        for node1 in self.graph.get_graph().nodes.values():
            for node2 in self.graph.get_graph().nodes.values():
                node_dist = find_dist_nodes(node1, node2)
                poke_dist = pokemon[2].dist_pokemon_node(node1) + pokemon[2].dist_pokemon_node(node2)
                # if the distances is almost equals
                if abs(node_dist - poke_dist) <= Epsilon:
                    # check the type_ in order to decide which one is SRC and which one is DST
                    if pokemon[2].type_ == 1:  # DST  > SRC
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

    def all_poke_src_dst(self):
        for pokemon in self.pokemons.Q:
            if pokemon[2].src is None and pokemon[2].dst is None:
                GameAlgo.find_poke_src_dst(self, pokemon)

    def cmd(self, client: Client):
        for a in self.agents.values():
            if a.dst == -1:
                if a.path:
                    client.choose_next_edge(
                        '{"agent_id":' + str(a.id) + ', "next_node_id":' + str(a.path.pop(0)) + '}')
                    # temp = a.path.pop(0)
                    # print('{"agent_id":' + str(a.id) + ', "next_node_id":' + str(temp) + '}')
                    if not a.path:
                        a.next_pokemon = None

    def beginning_of_the_game(self, client: Client):
        self.init_pokemons(client.get_pokemons())
        self.init_graph(client.get_graph())
        self.all_poke_src_dst()
        bla = client.get_info()
        bla_obj = json.loads(bla)
        for i in range(0, int(bla_obj['GameServer']['agents'])):
            client.add_agent('{\"id\":' + str(str(self.pokemons.pop().src)) + '}')

    def game_algorithm(self, client: Client):
        self.allocate_all_agents()
        self.cmd(client)
        client.move()

    def get_poke_list(self):
        return self.pokemons.get_poke_list()


PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'


def main():
    my_client = Client()
    my_client.start_connection(HOST, PORT)
    # bla = my_client.get_info()
    # blaObj = json.loads(bla)
    game = GameAlgo()
    # print("Hera re the pokemons")
    # game.init_pokemons(my_client.get_pokemons())
    # game.init_graph(my_client.get_graph())
    # print(game.pokemons)
    # game.all_pok_src_dst()
    # print(len(game.agents))
    # print(str(game.pokemons.pop().src))
    # for i in range(0 , int(blaObj['GameServer']['agents'])):
    # my_client.add_agent('{\"id\":'+ str(str(game.pokemons.pop().src)) +'}')
    # my_client.add_agent("{\"id\":1}")
    # my_client.add_agent("{\"id\":2}")
    # my_client.add_agent("{\"id\":3}")
    # my_client.start()

    # game = GameAlgo()
    # game.init_pokemons(my_client.get_pokemons())
    # game.init_graph(my_client.get_graph())
    game.beginning_of_the_game(my_client)
    # game.update_game(my_client.get_pokemons(), my_client.get_agents(), my_client.get_graph())
    pokes: str = my_client.get_pokemons()
    agns: str = my_client.get_agents()
    grp: str = my_client.get_graph()
    game.update_game(pokes, agns, grp)
    my_client.start()
    while my_client.is_running() == "true":
        game.update_game(my_client.get_pokemons(), my_client.get_agents())
        game.game_algorithm(my_client)
        # for a in game.agents.values():
        # print(a)
        print(my_client.time_to_end())
        print(my_client.get_info())
        time.sleep(0.1)
    # game.all_pok_src_dst()
    # game.init_agents(my_client.get_agents())
    # print(game.pokemons)
    # print(game.time_to_poke(0, 9))
    # print(game.time_to_poke(1, 9))
    # print(game.time_to_poke(2, 9))
    # temp = game.choose_agent()
    # print(temp)
    # print(game.agents.get(temp).path)
    my_client.stop_connection()
    print("Hello")
    exit(0)


if __name__ == "__main__":
    main()
