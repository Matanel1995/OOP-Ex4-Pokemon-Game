import math
from Ex3Files.Node import Node


class Pokemon:

    def __init__(self, value=-1, type_=-1, pos_=(-1, -1, -1)):
        self.value: float = value
        self.type_: int = type_
        self.pos: tuple[float] = pos_
        self.x_pos: float = self.pos[0]
        self.y_pos: float = self.pos[1]
        self.z_pos: float = self.pos[2]
        # SRC and DST values making it easy in the algo set for None for now
        self.src: int = -1
        self.dst: int = -1
        self.is_aget_allocated: bool = False
        self.curr_edge = None

    def dist_pokemon_node(self, node: Node):
        """this function will find the distance between pokemon and a Node
         will help later in finding SRC and DST of pokemon
         we use the regular distance formula d = sqrt((x1-x2)^2 + (y1-y2)^2)"""
        x_param = pow(node.pos[0] - self.x_pos, 2)
        y_param = pow(node.pos[1] - self.y_pos, 2)
        distance = math.sqrt(x_param + y_param)
        return distance

    def __str__(self):
        return "{\"Pokemon\": \"value\": " + f"{float(self.value)}" + ", \"type\": " + f"{int(self.type_)}" + \
               ", \"pos\": \"" + f"{float(self.x_pos)}" + "," + f"{float(self.y_pos)}" + "," + f"{float(self.z_pos)}" \
               + "\" }"
