from Pokemon import *


class Agent:
    def __init__(self, id_: int = -1, value_: float = -1, src_: int = -1, dest_: int = -1,
                 speed_: float = -1, pos_: tuple[float] = (-1, -1, -1)):
        self.id: int = id_
        self.value: float = value_
        self.src: int = src_
        self.dest: int = dest_
        self.speed: float = speed_
        self.pos = pos_
        self.x_pos = self.pos[0]
        self.y_pos = self.pos[1]
        self.z_pos = self.pos[2]
        self.next_pokemon = None
        self.path: list = list()

    def __str__(self):
        return '{"Agent":{"id":' + str(self.id) + ',"value":' + str(self.value) + ',"src":' + str(self.src) + \
               ',"dest":' + str(self.dest) + ',"speed":' + str(self.speed) + ',"pos":"' + str(self.x_pos) + ',' \
               + str(self.y_pos) + ',' + str(self.z_pos) + '"}'

    def str__next_edge(self):
        if not self.path:
            self.dest = self.path.pop(0)
        return '{"agent_id":' + str(self.id) + ', "next_node_id":' + str(self.dest) + '}'
