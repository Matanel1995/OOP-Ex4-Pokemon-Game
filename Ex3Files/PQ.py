import itertools
from heapq import *
from dataclasses import dataclass, field
from typing import Any

from Ex3Files import Node


class PQ(object):
    def __init__(self):
        self.Q = list()

    def add(self, node: Node):
        heappush(self.Q, (node.node_weight_curr, node.id))

    def pop(self):
        return heappop(self.Q)

    def push_pop(self, node: Node):
        return heappushpop(self.Q, (node.node_weight_curr, node.id))

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