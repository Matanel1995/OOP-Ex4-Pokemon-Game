import pygame
from pygame import *
import GameAlgo
from Ex3Files.GraphAlgo import *
from client import Client

radius = 40
black = (0,0,0)
white =(255,255,255)

WIDTH, HEIGHT = 1080, 720
clock = pygame.time.Clock()


class GameGui():

    pygame.init()
    pygame.display.set_caption("Pokemon: Catch the all!")

    def __init__(self, game):
            self.game = game
            self.pokemons = game.pokemons
            self.agents = game.agents
            self.graph = game.graph.get_graph()
            self.nodes = self.graph.nodes.values()
            self.edegs = self.graph.edges.values()
            self.max_x = 0
            self.max_y = 0
            self.min_x = sys.float_info.max
            self.min_y = sys.float_info.max

            self.screen = pygame.display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
            self.is_running = True
            self.clock = pygame.time.Clock()
            for node in self.nodes:
                self.max_x = max(self.max_x, node.pos[0])
                self.max_y = max(self.max_y, node.pos[1])
                self.min_x = min(self.min_x, node.pos[0])
                self.min_y = min(self.min_y, node.pos[1])

    def init_screen(self):
        Background_img = pygame.image.load('Pokemon_Background.png')
        w, h = pygame.display.get_surface().get_size()
        Background_img = pygame.transform.scale(Background_img, (w, h))
        self.screen.blit(Background_img, [0, 0])
        self.draw_nodes()
        self.draw_edegs()
        #display.update()

    def update_gui(self,game:GameAlgo ,Client:Client):

        data = json.loads(Client.get_info())["GameServer"]

        font = pygame.font.Font('freesansbold.ttf', 14)
        currTime = Client.time_to_end()
        text_To_Finish = font.render('Time to finish: ' + str(int(currTime) / 1000) + ' sec.', True, black)
        textRect_To_Finish = text_To_Finish.get_rect()
        text_To_Finish.set_alpha(127)
        textRect_To_Finish.center = (90, 10)
        textRect_To_Finish.left = 5

        text_Move = font.render('Moves : ' + str(data['moves']), True, black)
        textRect_Move = text_Move.get_rect()
        text_Move.set_alpha(127)
        textRect_Move.center = (41, 30)
        textRect_Move.left = 5

        text_OverallPoints = font.render('Total points so far : ' + str(data['grade']), True, black)
        textRect_OverallPoints = text_OverallPoints.get_rect()
        text_OverallPoints.set_alpha(127)
        textRect_OverallPoints.center = (75, 50)
        textRect_OverallPoints.left = 5

        Background_img = pygame.image.load('Pokemon_Background.png')
        w, h = pygame.display.get_surface().get_size()
        Background_img = pygame.transform.scale(Background_img, (w, h))

        self.screen.blit(Background_img, [0, 0])
        self.screen.blit(text_To_Finish, textRect_To_Finish)
        self.screen.blit(text_Move, textRect_Move)
        self.screen.blit(text_OverallPoints, textRect_OverallPoints)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                return False
        self.draw_nodes()
        self.draw_edegs()
        self.draw_agent()
        self.draw_pokemon()

        display.update()
        clock.tick(60)

    def draw_nodes(self):
        Pokeball_img = pygame.image.load('Pokeball.png').convert_alpha()
        Pokeball_img = pygame.transform.scale(Pokeball_img, (radius, radius))

        # draw nodes
        for n in self.nodes:
            x, y, _ = str(n.pos).split(',')
            x = x[1:]
            y = y[1:]
            x = self.my_scale(float(x), x=True)
            y = self.my_scale(float(y), y=True)

            self.screen.blit(Pokeball_img, (int(x) - int(radius / 2), int(y) - int(radius / 2)))

            # draw the node id
            FONT = pygame.font.SysFont('Arial', 20, bold=True)
            id_srf = FONT.render(str(n.id), True, Color(0, 0, 230))
            rect = id_srf.get_rect(center=(x, y - 28))
            self.screen.blit(id_srf, rect)

    def draw_edegs(self):
        # draw edges
        for src, node in self.graph.nodes.items():
            src = self.graph.nodes.get(src)
            for dst, w in node.edges_out.items():
                # find the edge nodes
                # GameGui.edge_iter(self.graph)
                # src = next(n for n in self.nodes if n.id == e.src)
                # dest = next(n for n in self.nodes if n.id == e.dest)
                dst = self.graph.nodes.get(dst)
                src_x, src_y, _ = str(src.pos).split(',')
                src_x = src_x[1:]
                src_y = src_y[1:]
                dst_x, dst_y, _ = str(dst.pos).split(',')
                dst_x = dst_x[1:]
                dst_y = dst_y[1:]
                # scaled positions
                src_x = self.my_scale(float(src_x), x=True)
                src_y = self.my_scale(float(src_y), y=True)
                dst_x = self.my_scale(float(dst_x), x=True)
                dst_y = self.my_scale(float(dst_y), y=True)

                # draw the line
                pygame.draw.line(self.screen, Color(61, 72, 126),
                                 (src_x, src_y), (dst_x, dst_y))

    def draw_agent(self):
        Pokemon_Mester_img = pygame.image.load('Pokemon_Master.png').convert_alpha()
        Pokemon_Mester_img = pygame.transform.scale(Pokemon_Mester_img, (radius - 10, radius - 10))
        agents = self.game.agents
        for a in agents.items():
            x = self.my_scale(float(a[1].x_pos), x=True)
            y = self.my_scale(float(a[1].y_pos), y=True)
            self.screen.blit(Pokemon_Mester_img, (int(x) -10 , int(y) -10))

    def draw_pokemon(self):
        Charizard_img = pygame.image.load('Charizard.png').convert_alpha()
        Charizard_img = pygame.transform.scale(Charizard_img, (radius, radius))
        pokemons = self.pokemons.Q
        for p in pokemons:
            x = self.my_scale(float(p[2].x_pos) , x=True)
            y = self.my_scale(float(p[2].y_pos), y=True)
            self.screen.blit(Charizard_img, (int(x) - 10, int(y) - 17))


    def scale(self, data, min_screen, max_screen, min_data, max_data):
        """
        get the scaled data with proportions min_data, max_data
        relative to min and max screen dimentions
        """
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


    # decorate scale with the correct values
    def my_scale(self,data, x=False, y=False):
        if x:
            return self.scale(data, 50, self.screen.get_width() - 50, self.min_x, self.max_x)
        if y:
            return self.scale(data, 50, self.screen.get_height() - 50, self.min_y, self.max_y)


def main(game: GameAlgo):
    gui = GameGui(game)


if __name__ == "__main__":
    main()
