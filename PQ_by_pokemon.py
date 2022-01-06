from heapq import *

from Pokemon import *


class PQByPokemon(object):
    def __init__(self):
        self.Q = list()

    def add(self, poke: Pokemon):
        heappush(self.Q, ((-1) * poke.value, poke))

    def pop(self):
        return heappop(self.Q)

    def push_pop(self, poke: Pokemon):
        return heappushpop(self.Q, ((-1) * poke.value, poke))

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
