import math
from Ex3Files.Node import Node

default_pokemon: dict = {"value": -1, "type": 0, "pos": "-1,-1,0"}


class Pokemon:
    def __init__(self, pokemon_info=None):
        if pokemon_info is None:
            pokemon_info = default_pokemon
        self.value: float = float(pokemon_info['value'])
        self.type_: int = int(pokemon_info['type'])
        self.pos = tuple(map(float, pokemon_info['pos'].split(',')))
        self.x_pos = self.pos[0]
        self.y_pos = self.pos[1]
        self.z_pos = self.pos[2]
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

    def __str__(self):
        return "{\"Pokemon\": \"value\": " + f"{float(self.value)}" + ", \"type\": " + f"{int(self.type_)}" + \
               ", \"pos\": \"" + f"{float(self.x_pos)}" + "," + f"{float(self.y_pos)}" + "," + f"{float(self.z_pos)}" \
               + "\" }"


def gen_pokemon(value: float, type_: int, x_: float, y_: float, z_: float) -> Pokemon:
    return Pokemon({"value": value, "type": type_, "pos": str(x_) + ',' + str(y_) + ',' + str(z_)})
