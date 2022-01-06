import math
from files_from_Ex3.Node import Node



class Pokemon:
    def __init__(self, pokemon_info: dict):
        self.value = float(pokemon_info['value'])
        self.type = int(pokemon_info['type'])
        self.pos = str(pokemon_info['pos'])
        split_pos = self.pos.split(',')
        self.x_pos = split_pos[0]
        self.y_pos = split_pos[1]
        # SRC and DST values making it easy in the algo set for None for now
        self.src = None
        self.dst = None
        self.is_aget_allocated = False
        self.curr_edge = None

    def dist_pokemon_node(self, node: Node):
        # this function will find the distance between pokemon and a Node
        # will help later in finding SRC and DST of pokemon
        # we use the regular distance formula d = sqrt((x1-x2)^2 + (y1-y2)^2)
        x_param = pow(node.pos[0] - self.x_pos, 2)
        y_param = pow(node.pos[1] - self.y_pos, 2)
        distance = math.sqrt(x_param + y_param)
        return distance
