from dataclasses import dataclass, field
from typing import Any
from heapq import *

import Pokemon


@dataclass(order=True)
class PrioritizedItem:
    priority: float
    item: Any = field(compare=False)

    # def __eq__(self, other):
    #     return self.priority == other.priority
    #
    # def __lt__(self, other):
    #     return self.priority < other.priority
    #
    # def __gt__(self, other):


class PQByPokemon(object):
    def __init__(self):
        self.Q = list()
        self.n: int = 0

    def add(self, poke: Pokemon):
        heappush(self.Q, ((-1) * poke.value, self.n, poke))
        self.n += 1

    def pop(self):
        return heappop(self.Q)

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
