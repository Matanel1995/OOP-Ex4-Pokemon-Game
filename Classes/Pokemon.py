import math
from Ex3Files.Node import Node


class Pokemon:
    def __init__(self, pokemon_info: dict):
        self.value: float = float(pokemon_info['value'])
        self.type_: int = int(pokemon_info['type'])
        self.pos = str(pokemon_info['pos'])
        split_pos = self.pos.split(',')
        self.x_pos = split_pos[0]
        self.y_pos = split_pos[1]
        self.z_pos = split_pos[2]
        # SRC and DST values making it easy in the algo set for None for now
        self.src = None
        self.dst = None
        self.is_aget_allocated = False

    def dist_pokemon_node(self, node: Node):
        """this function will find the distance between pokemon and a Node
        will help later in finding SRC and DST of pokemon
        we use the regular distance formula d = sqrt((x1-x2)^2 + (y1-y2)^2)"""
        x_param = pow(float(node.pos[0]) - float(self.x_pos), 2)
        y_param = pow(float(node.pos[1]) - float(self.y_pos), 2)
        distance = math.sqrt(x_param + y_param)
        return distance
