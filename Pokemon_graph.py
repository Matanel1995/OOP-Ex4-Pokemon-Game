from Ex3Files import GraphAlgo
from Classes import Pokemon, Agent


class PokemonGraph:
    def __init__(self, ga: GraphAlgo):
        self.my_algo = ga
        self.agents: dict[Agent] = dict()
        self.pokemons: dict[Pokemon] = dict()
        self.poke_num: int = 0
        self.agent_num: int = 0

    def time_to_poke(self, agent_id: int, poke_src: int) -> float:
        agent = self.agents.get(agent_id)
        dist = self.my_algo.shortest_path(agent.curr_node, poke_src)[0]
        return dist / agent.speed
