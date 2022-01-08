import json
from pygame import gfxdraw
import pygame
from pygame import *
from temp_client import *
# init pygame

WIDTH, HEIGHT = 1080, 720

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

# get the graph
GAME_ALGO=
GRAPH = GAME_ALGO.graph

POKEMONS: list = GAME_ALGO.get_poke_list()
AGENTS = GAME_ALGO.agents

FONT = pygame.font.SysFont('Arial', 20, bold=True)
