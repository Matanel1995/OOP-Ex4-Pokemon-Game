import json
from collections import deque
from itertools import permutations
from typing import List

from Ex3Files.DiGraph import *
from Ex3Files.GUI_PyGame import plot_graph
from Ex3Files.Node import *
from Ex3Files.PQ import *


def st_path(src: int, dest: int):
    return src.__str__() + "to" + dest.__str__()


class GraphAlgo:
    paths: dict

    def __init__(self, g=DiGraph()):
        self.my_graph = g
        self.paths = dict()

    def set_my_graph(self, new_graph: DiGraph):
        self.my_graph = new_graph

    def get_graph(self) -> DiGraph:
        return self.my_graph

    def load_from_json(self, file_name: Any) -> bool:
        try:
            self.my_graph.edgesNum = 0
            self.my_graph.nodesNum = 0
            self.my_graph.mc = 0
            if 'Nodes' in file_name:
                self.my_graph.nodes = dict()
                for node in file_name['Nodes']:
                    if 'pos' in node:
                        temp_pos = tuple(map(float, node['pos'].split(',')))
                    else:
                        temp_pos = None
                    temp_id: int = node['id']
                    self.my_graph.add_node(temp_id, temp_pos)
                if 'Edges' in file_name:
                    self.my_graph.edges = dict()
                    for edge in file_name['Edges']:
                        temp_src: int = edge['src']
                        temp_dest: int = edge['dest']
                        if 'w' in edge:
                            temp_w: float = edge['w']
                        else:
                            temp_w: float = 0
                        self.my_graph.add_edge(temp_src, temp_dest, temp_w)
                        self.my_graph.mc = 0
            return True
        except FileNotFoundError:
            print("No such file, please check your files and location")

    # def save_to_json(self, file_name: str) -> bool:
    #     json_file = json.loads(self.my_graph.__str__())
    #     with open(file_name, 'w') as output_file:
    #         json.dump(json_file, output_file, indent=2)
    #     load_json = GraphAlgo()
    #     load_json.load_from_json(file_name)
    #     if self.my_graph.__str__() == load_json.my_graph.__str__():
    #         return True
    #     else:
    #         return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """The distance of the path, a list of the nodes ids that the path goes through
        Notes:
        If there is no path between id1 and id2, or one of them does not exist the function returns (float('inf'),[])"""
        if id1 not in self.my_graph.nodes.keys() or id2 not in self.my_graph.nodes.keys():
            return MAX_FLOAT, []
        self.diakstra(id1)
        if self.get_node_w(id2) == MAX_FLOAT:
            return float('inf'), []
        else:
            return self.get_node_w(id2), self.get_prev_list(id1, id2)

    def diakstra(self, src: int):
        pq = PQ()
        # initialize all parameters
        for id, node in self.my_graph.nodes.items():
            node.set_prev_node(-1)
            node.tag = WHITE
            if id == src:
                node.set_node_weight(0)
            else:
                node.set_node_weight(MAX_FLOAT)
        pq.add(self.my_graph.nodes.get(src))
        while not pq.is_empty():
            curr_id: int = pq.pop()[1]
            curr_node: Node = self.get_node(curr_id)
            if self.get_node_tag(curr_id) == WHITE:
                self.my_graph.nodes.get(curr_id).tag = BLACK
                for destID, w in curr_node.edges_out.items():
                    if self.get_node_tag(destID) == WHITE:
                        self.relax(curr_id, destID)
                        for id in self.my_graph.nodes.get(curr_id).edges_out.keys():
                            pq.add(self.get_node(id))

    def relax(self, src: int, dest: int):
        if self.get_node_w(dest) > (self.get_node_w(src) + self.get_edge_w(src, dest)):
            self.set_path_w(dest, self.get_node_w(src) + self.get_edge_w(src, dest))
            self.set_prev_node(dest, src)

    def get_prev_list(self, src: int, dest: int) -> list:
        """Returns a list of the nodes ids that the path goes through"""
        li = list()
        curr_path = self.get_node_w(dest)
        if curr_path == MAX_FLOAT:
            return li
        li.append(dest)
        curr_node: int = dest
        while li[0] != src and curr_path > 0:
            curr_node = self.get_prev_node(curr_node)
            li.insert(0, curr_node)
            curr_path = self.get_node_w(curr_node)
        return li

    def get_node_w(self, id: int):
        return self.my_graph.nodes.get(id).node_weight_curr

    def get_node(self, id: int) -> Node:
        return self.my_graph.nodes.get(id)

    def get_node_tag(self, id: int):
        return self.my_graph.nodes.get(id).tag

    def set_node_tag(self, id: int, tag):
        self.my_graph.nodes.get(id).set_tag(tag)

    def get_edge_w(self, src: int, dest: int):
        return self.my_graph.edges.get(st_edge(src, dest))

    def set_path_w(self, id: int, w: float):
        self.my_graph.nodes.get(id).node_weight_curr = w

    def get_prev_node(self, node_id: int):
        return self.my_graph.nodes.get(node_id).prevNodeID

    def set_prev_node(self, curr_id: int, prev_id: int):
        self.my_graph.nodes.get(curr_id).set_prev_node(prev_id)

    #   tsp3
    def TSP(self, node_lst: List[int]) -> (List[int], float):
        min_dist = MAX_FLOAT
        returned_path = list()
        dist = 0
        for first_node in node_lst:
            if self.tsp_all_permutations(first_node, node_lst)[1] < min_dist:
                min_dist = self.tsp_all_permutations(first_node, node_lst)[1]
                returned_path, dist = self.tsp_all_permutations(first_node, node_lst)
        if min_dist == MAX_FLOAT:
            return [], float('inf')
        return returned_path, dist

    def tsp_all_permutations(self, first_node, node_lst):
        returned_path = []
        curr_path = []
        temp_list = []
        for node_id in node_lst:
            if node_id != first_node:
                temp_list.append(node_id)

        min_dist = MAX_FLOAT
        # permutations of all the nodes using the function imported from itertools
        all_list_permutations = permutations(temp_list)

        for curr_permutation in all_list_permutations:
            curr_path.clear()
            path_is_minimal = True
            curr_weight = 0
            curr_src = first_node
            curr_path.append(curr_src)

            for perm in curr_permutation:
                w = self.shortest_path(curr_src, perm)[0]
                for index in range(len(self.shortest_path(curr_src, perm)[1])):
                    if index != 0:
                        curr_path.append(self.shortest_path(curr_src, perm)[1][index])
                if w == float('inf'):
                    path_is_minimal = False
                    break
                curr_weight += w
                curr_src = perm
            if path_is_minimal:
                if min_dist > curr_weight:
                    min_dist = curr_weight
                    returned_path = curr_path
        return returned_path, min_dist

    # def tsp2(self, node_lst: List[int]) -> (List[int], float):
    #     min_ = MAX_FLOAT
    #     returned_path = list()
    #     for src_id, src_node in self.my_graph.nodes.items():
    #         self.diakstra(src_id)
    #         pq = PQ()
    #         for dest_id in node_lst:
    #             if dest_id != src_id:
    #                 temp_n = Node(dest_id)
    #                 temp_n.set_node_weight(self.get_node_w(dest_id))
    #                 pq.add(temp_n)
    #         sum_ = 0
    #         temp_path = list()
    #         temp_curr_id = src_id
    #         temp_curr_tuple = (src_id, 0)
    #         temp_path.append(temp_curr_id)
    #         while not pq.is_empty():
    #             sum_ += self.shortest_path(temp_curr_id, pq.peek()[1])[0]
    #             temp_curr_id = pq.peek()[1]
    #             temp_path.append(pq.pop()[1])
    #         if sum_ < min_:
    #             min_ = sum_
    #             returned_path = temp_path
    #     return returned_path, min

    #   OG tsp
    # def og_tsp(self, node_lst: List[int]) -> (List[int], float):
    #     min_dist = MAX_FLOAT
    #     returned_path = list()
    #     for src_id_curr in node_lst:
    #         pq = PQ()
    #         for dest_id_curr in node_lst:
    #             if dest_id_curr != src_id_curr:
    #                 temp_node = Node(dest_id_curr)
    #                 short_dist = self.shortest_path(src_id_curr, dest_id_curr)
    #                 temp_node.set_node_weight(short_dist[0])
    #                 pq.add(temp_node)
    #         sum_path: float = 0
    #         temp_path = list()
    #         temp_path.append(src_id_curr)
    #         while not pq.is_empty():
    #             short_dist = self.shortest_path(src_id_curr, pq.peek())
    #             sum_path += short_dist[0]
    #             temp_path.append(pq.pop())
    #         if sum_path < min_dist:
    #             min_dist = sum_path
    #             returned_path = temp_path
    #     if min_dist == MAX_FLOAT:
    #         return None, float('inf')
    #     else:
    #         return returned_path, min_dist

    # def centerPoint(self) -> (int, float):
    #     if self.is_connected__():
    #         tup = self.center_point_help()
    #         return tup[0], tup[1]
    #     else:
    #         return None, float('inf')

    # def center_point_help(self) -> (int, float, list):
    #     center_node_id: int = -1
    #     center_dist: float = MAX_FLOAT
    #     center_li = list()
    #     for id1, node1 in self.my_graph.nodes.items():
    #         self.diakstra(id1)
    #         max_dist: float = -1
    #         curr_max_node_id: int = -1
    #         max_li = list()
    #         for id2, node2 in self.my_graph.nodes.items():
    #             w2 = self.get_node_w(id2)
    #             if w2 < MAX_FLOAT:
    #                 if w2 > max_dist and w2 != -1:
    #                     max_dist = w2
    #                     curr_max_node_id = id1
    #                     max_li = self.get_prev_list(id1, id2)
    #         if center_dist > max_dist:
    #             center_dist = max_dist
    #             center_li = max_li
    #             center_node_id = curr_max_node_id
    #     return center_node_id, center_dist, center_li
    #
    # # def plot_graph(self) -> None:
    # #     plot_graph(self.my_graph)
    #
    # def is_connected__(self):
    #     for src_id, src_node in self.my_graph.nodes.items():
    #         for dest_id, dest_node in self.my_graph.nodes.items():
    #             short_dist = self.shortest_path(src_id, dest_id)
    #             if short_dist[0] == MAX_FLOAT or short_dist[0] == float('inf'):
    #                 return False
    #     return True
