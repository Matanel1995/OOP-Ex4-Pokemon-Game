from Classes import Pokemon
from heapq import *


class PQByPokemon(object):
    def __init__(self):
        self.Q = list()
        self.n: int = 0

    def add(self, poke: Pokemon):
        heappush(self.Q, ((-1) * poke.value, self.n, poke))
        self.n += 1

    def pop(self):
        return heappop(self.Q)[2]

    def push_pop(self, poke: Pokemon):
        heappushpop(self.Q, ((-1) * poke.value, self.n, poke))
        self.n += 1

    def get_w(self, i: int):
        return self.Q[i][0]

    def get_id(self, i: int):
        return self.Q[i][1]

    def is_empty(self):
        return len(self.Q) == 0

    def size(self):
        return len(self.Q)

    def __str__(self):
        return self.Q.__str__()

    def peek(self) -> tuple:
        return self.Q[0]

    def peek_pokemon(self) -> Pokemon:
        return self.Q[0][2]

    def peek_val(self) -> float:
        return self.Q[0][2].value

    def peek_pos(self) -> tuple:
        return self.Q[0][2].pos

    def peek_src(self) -> int:
        return self.Q[0][2].src

    def peek_dst(self) -> int:
        return self.Q[0][2].dst

    def get_poke_list(self):
        """returns self.Q - a list of all the pokemons, NOT SORTED"""
        return self.Q
