import random

import json

from Node import *


def st_edge(src: int, dest: int):
    return src.__str__() + "to" + dest.__str__()


class DiGraph:
    nodes: dict = None
    edges: dict = None
    mc: int = None
    edgesNum: int = None
    nodesNum: int = None

    def __init__(self):
        self.edges = dict()
        self.nodes = dict()
        self.mc = 0
        self.edgesNum = 0
        self.nodesNum = 0

    def v_size(self) -> int:
        return self.nodesNum

    def e_size(self) -> int:
        return self.edgesNum

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes.get(id1).edges_in

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes.get(id1).edges_out

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodes and id2 in self.nodes and st_edge(id1, id2) not in self.edges:
            self.nodes.get(id1).add_outgoing_edge(id2, weight)
            self.nodes.get(id2).add_incoming_edge(id1, weight)
            self.edges[st_edge(id1, id2)] = weight
            self.edgesNum += 1
            if self.mc >= 0:
                self.mc += 1
            return True
        elif id1 not in self.nodes or id2 not in self.nodes or st_edge(id1, id2) in self.edges:
            pass
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.nodes:
            if pos is None:
                x_coordinate: float = random.uniform(0, 1500)
                y_coordinate: float = random.uniform(0, 900)
                z_coordinate: float = random.uniform(0, MAX_FLOAT / 2)
                pos = (x_coordinate, y_coordinate, z_coordinate)
            temp = Node(node_id, pos)
            self.nodes[temp.id] = temp
            self.nodesNum += 1
            if self.mc >= 0:
                self.mc += 1
            return True
        else:
            pass
        return False

    def add__node(self, n: Node):
        if n.id not in self.nodes:
            self.nodes[n.id] = n
        else:
            pass

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            pass
        elif node_id in self.nodes:
            for in_ in list(self.nodes.get(node_id).edges_in.keys()):
                self.remove_edge(in_, node_id)
            for out_ in list(self.nodes.get(node_id).edges_out.keys()):
                self.remove_edge(node_id, out_)
            if self.mc >= 0:
                self.mc += 1
            self.nodes.pop(node_id)
            self.nodesNum -= 1
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if st_edge(node_id1, node_id2) in self.edges:
            self.nodes.get(node_id1).delete_outgoing_edge(node_id2)
            self.nodes.get(node_id2).delete_incoming_edge(node_id1)
            self.edges.pop(st_edge(node_id1, node_id2))
            if self.mc >= 0:
                self.mc += 1
            self.edgesNum -= 1
            return True
        elif node_id1 not in self.nodes or node_id2 not in self.nodes:
            pass
        else:
            return False

    def edges_str(self):
        first_e = True
        st = "  \"Edges\": [\n"
        for key, w in self.edges.items():
            key_temp = tuple(map(float, key.split('to')))
            src_temp = key_temp[0]
            dest_temp = key_temp[1]
            if first_e is False:
                st += ",\n"
            else:
                first_e = False
            st += "    {\n      \"src\": " + f"{int(src_temp)}" + ",\n      \"w\": " + \
                  f"{float(w)}" + ",\n      \"dest\": " + f"{int(dest_temp)}" + "\n    }"
        return st + "\n  ]"

    def nodes_str(self):
        first_n = True
        st = "  \"Nodes\": [\n"
        for n in self.nodes.values():
            if first_n is False:
                st += ",\n"
            else:
                first_n = False
            st += "    {\n      " + f"{n}" + "\n    }"
        return st + "\n  ]"

    def __str__(self):
        return "{\n" + self.edges_str() + ",\n" + self.nodes_str() + "\n}"

    def __repr__(self):
        """
        different output - as in main:
            return "Graph: |V|="+f"{self.v_size()}"+" , |E|="+f"{self.e_size()}"+"\n"
        """
        return "Graph: |V|=" + f"{self.v_size()}" + " , |E|=" + f"{self.e_size()}"
