from Pokemon import *


class Agent:
    def __init__(self, agent_info: dict):
        self.id: int = int(agent_info['id'])
        self.value: float = float(agent_info['value'])
        self.src: int = int(agent_info['src'])
        self.dest: int = int(agent_info['dest'])
        self.speed: float = float(agent_info['speed'])
        self.pos = str(agent_info['pos'])
        split_pos = self.pos.split(',')
        self.x_pos = split_pos[0]
        self.y_pos = split_pos[1]
        self.z_pos = split_pos[2]
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
