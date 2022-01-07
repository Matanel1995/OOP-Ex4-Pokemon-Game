from heapq import *

from Classes.Pokemon import *


class PQByPokemon(object):
    def __init__(self):
        self.Q = list()
        self.n: int = 0

    def add(self, poke: Pokemon):
        self.n += 1
        heappush(self.Q, ((-1) * poke.value, self.n, poke))

    def pop(self):
        return heappop(self.Q)[2]

    def push_pop(self, poke: Pokemon):
        self.n += 1
        heappushpop(self.Q, ((-1) * poke.value, self.n, poke))

    def is_empty(self):
        return len(self.Q) == 0

    def size(self):
        return len(self.Q)

    def __str__(self):
        return self.Q.__str__()

    def peek(self):
        return self.Q[2]

    def peek_val(self) -> float:
        return self.Q[2].value

    def peek_pos(self) -> tuple:
        return self.Q[2].pos

    def peek_src(self) -> int:
        return self.Q[2].src

    def peek_dst(self) -> int:
        return self.Q[2].dst
