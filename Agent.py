from Pokemon import *


class Agent:
    def __init__(self, agent_info: dict):
        self.id: int=int(agent_info['id'])
        self.value: float=float(agent_info['value'])
        self.src: int=int(agent_info['src'])
        self.dest: int=int(agent_info['dest'])
        self.speed: float=float(agent_info['speed'])
        self.grade: float=float(agent_info['grade'])
        self.pos = str(agent_info['pos'])
        split_pos = self.pos.split(',')
        self.x_pos = split_pos[0]
        self.y_pos = split_pos[1]
        self.z_pos = split_pos[2]
        self.next_pokemon = None

