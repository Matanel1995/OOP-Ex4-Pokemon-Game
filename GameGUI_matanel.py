import pygame
from pygame import *
import GameAlgo
from Ex3Files.GraphAlgo import *

radius = 40
black = (0, 0, 0)
white = (255, 255, 255)

WIDTH, HEIGHT = 1080, 720
clock = pygame.time.Clock()


class GameGui:
    pygame.init()
    pygame.display.set_caption("Pokemon: Catch the all!")

    def __init__(self, game):
        if not game:
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

            self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            self.is_running = True
            self.clock = pygame.time.Clock()
            for node in self.nodes:
                self.max_x = max(self.max_x, node.pos[0])
                self.max_y = max(self.max_y, node.pos[1])
                self.min_x = min(self.min_x, node.pos[0])
                self.min_y = min(self.min_y, node.pos[1])

    def init_screen(self):
        Pokeball_img = pygame.image.load('Pokeball.png').convert_alpha()
        Pokeball_img = pygame.transform.scale(Pokeball_img, (radius, radius))

        # draw nodes
        for n in self.graph.get_graph.nodes:
            x = self.my_scale(n.pos.x, x=True)
            y = self.my_scale(n.pos.y, y=True)

            self.screen.blit(Pokeball_img, (int(x) - int(radius / 2), int(y) - int(radius / 2)))

            # draw the node id
            FONT = pygame.font.SysFont('Arial', 20, bold=True)
            id_srf = FONT.render(str(n.id), True, Color(0, 0, 230))
            rect = id_srf.get_rect(center=(x, y - 28))
            self.screen.blit(id_srf, rect)

        # draw edges
        for e in self.graph.get_graph.edges:
            # find the edge nodes
            src = next(n for n in self.graph.get_graph.nodes if n.id == e.src)
            dest = next(n for n in self.graph.get_graph.nodes if n.id == e.dest)

            # scaled positions
            src_x = self.my_scale(src.pos.x, x=True)
            src_y = self.my_scale(src.pos.y, y=True)
            dest_x = self.my_scale(dest.pos.x, x=True)
            dest_y = self.my_scale(dest.pos.y, y=True)

            # draw the line
            pygame.draw.line(self.screen, Color(61, 72, 126),
                             (src_x, src_y), (dest_x, dest_y))

    def scale(self, data, min_screen, max_screen, min_data, max_data):
        """
        get the scaled data with proportions min_data, max_data
        relative to min and max screen dimentions
        """
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

    # decorate scale with the correct values
    def my_scale(self, data, x=False, y=False):
        if x:
            return self.scale(data, 50, self.screen.get_width() - 50, self.min_x, self.max_x)
        if y:
            return self.scale(data, 50, self.screen.get_height() - 50, self.min_y, self.max_y)


def main(game: GameAlgo):
    gui = GameGui(game)


if __name__ == "__main__":
    main()
