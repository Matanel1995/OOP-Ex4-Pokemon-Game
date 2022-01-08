import sys

WHITE = -1
GREY = 0
BLACK = 1
MAX_FLOAT = sys.float_info.max


class Node:
    id: int = None
    pos: tuple = None
    # x_coordinate: float
    # y_coordinate: float
    # z_coordinate: float
    key: int = None
    tag: int = None
    prevNodeID: int = None
    edges_in: dict = None
    edges_out: dict = None
    node_weight_curr: float = None

    def __init__(self, id: int = 0, pos: tuple = (0, 0, 0)):
        self.id = id
        # self.x_coordinate = pos[0]
        # self.y_coordinate = pos[1]
        # self.z_coordinate = pos[2]
        self.pos = pos
        self.key = self.id
        self.tag = WHITE
        self.prevNodeID = -1
        self.edges_in = dict()
        self.edges_out = dict()
        self.node_weight_curr: float = MAX_FLOAT

    def get_key(self):
        return self.id

    def add_incoming_edge(self, src: int, w: float):
        if src not in self.edges_in:
            self.edges_in[src] = w

    def add_outgoing_edge(self, dest: int, w: float):
        if dest not in self.edges_out:
            self.edges_out[dest] = w

    def delete_node(self, node_id: int):
        self.edges_in.pop(node_id)
        self.edges_out.pop(node_id)

    def delete_incoming_edge(self, src_id: int):
        if src_id in self.edges_in:
            del self.edges_in[src_id]
        # self.edges_in.pop(src_id)

    def delete_outgoing_edge(self, dest_id: int):
        if dest_id in self.edges_out:
            del self.edges_out[dest_id]
        # self.edges_out.pop(dest_id)

    def set_node_weight(self, w):
        self.node_weight_curr = w

    def set_prev_node(self, prev_id: int):
        self.prevNodeID = prev_id

    def set_tag(self, tag):
        self.tag = tag

    def __str__(self):
        st = "\"pos\": \"" + f"{float(self.pos[0])}" + "," + f"{float(self.pos[1])}" + "," \
             + f"{float(self.pos[2])}" + "\",\n      \"id\": " + f"{self.id}"
        # st="{"+f"{self.id}"+": "+f"{self.id}"+": |edges"

        return st