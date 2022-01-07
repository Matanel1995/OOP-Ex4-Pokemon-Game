default_agent: dict = {"id": -1, "value": -1, "src": -1, "dest": -1, "speed": -1, "pos": "-1,-1,0"}


class Agent:

    def __init__(self, agent_info=None):
        if agent_info is None:
            agent_info = default_agent
        self.id: int = int(agent_info['id'])
        self.value: float = float(agent_info['value'])
        self.src: int = int(agent_info['src'])
        self.dst: int = int(agent_info['dest'])
        self.speed: float = float(agent_info['speed'])
        self.pos = tuple(map(float, agent_info['pos'].split(',')))
        self.x_pos = self.pos[0]
        self.y_pos = self.pos[1]
        self.z_pos = self.pos[2]
        self.next_pokemon = None
        self.path: list = list()

    def __str__(self):
        return '{"Agent":{"id":' + str(self.id) + ',"value":' + str(self.value) + ',"src":' + str(self.src) + \
               ',"dest":' + str(self.dst) + ',"speed":' + str(self.speed) + ',"pos":"' + str(self.x_pos) + ',' \
               + str(self.y_pos) + ',' + str(self.z_pos) + '"}'


def gen_agent(id: int, value: float, src: int, dest: int, speed: float, x_: float, y_: float, z_: float) -> Agent:
    return Agent({"id": id, "value": value, "src": src, "dest": dest, "speed": speed,
                  "pos": str(x_) + ',' + str(y_) + ',' + str(z_)})
