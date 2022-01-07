import sys

import pygame
from pygame import *

from Ex3Files.GraphAlgo import *
from GUI.Button import *

FPS = 60
radius = 40
WIDTH, HEIGHT = 900, 500
# screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

# Colors:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (127, 0, 255)
PINK = (255, 0, 255)
ORANGE = (255, 128, 0)
LIGHT_RED = (255, 153, 153)
LIGHT_GREEN = (153, 255, 153)
LIGHT_BLUE = (153, 204, 255)
LIGHT_YELLOW = (255, 255, 153)
LIGHT_PURPLE = (204, 153, 255)
LIGHT_PINK = (255, 204, 255)
LIGHT_ORANGE = (255, 204, 153)
LIGHT_GREY = (192, 192, 192)
DARK_RED = (102, 0, 0)
DARK_GREEN = (0, 102, 0)
DARK_BLUE = (0, 0, 102)
DARK_PURPLE = (51, 0, 102)


def refresh_screen(screen):
    # Loading all the images
    background_img = pygame.image.load('img_files/Pokemon_Background.png')
    pokeball_img = pygame.image.load('img_files/Pokeball.png').convert_alpha()
    pokeball_img = pygame.transform.scale(pokeball_img, (radius, radius))
    pokemon_mester_img = pygame.image.load('img_files/Pokemon_Master.png').convert_alpha()
    pokemon_mester_img = pygame.transform.scale(pokemon_mester_img, (radius - 10, radius - 10))


def get_graph(graph_str):
    graph_a = GraphAlgo()
    graph_a.load_from_json(graph_str)
    return graph_a


def main():
    clock = pygame.time.Clock()
    pygame.font.init()
    pygame.init()
    run = True
    fullscreen = False
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Ex4 - gotta catch 'em all!")
    monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
    mx, my = pygame.mouse.get_pos()

    stop_button = Button(screen.get_width() - 5 - (screen.get_width() / 5), 50, 100, 40, 'STOP')

    while run:
        screen.fill(WHITE)

        pygame.draw.rect(screen, PURPLE,
                         pygame.Rect(screen.get_width() - 5 - (screen.get_width() / 5), 50, screen.get_width() / 5, 50))
        stop_button.draw(screen)

        clock.tick(FPS)
        for event_ in pygame.event.get():
            if event_.type == pygame.QUIT:
                run = False
            if event_.type == VIDEORESIZE:
                if not fullscreen:
                    screen = pygame.display.set_mode((event_.w, event_.h), pygame.RESIZABLE)
            if event_.type == KEYDOWN:
                if event_.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event_.key == K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
