import pygame
from pygame import *
from GameGUI import *
from Classes.Pokemon import *

# Charizard_path = 'GUI/Charizard.png'
# Eevee_path = 'GUI/eevee.jpeg'
# Magikarp_path = 'GUI/magikarp.jpeg'
# Pikachu_path = 'GUI/pikachu.jpeg'
# Snorlax_path = 'GUI/snorlax.jpeg'
# Squirtle_path = 'GUI/squirtle.jpeg'

Charizard_img = pygame.image.load('img_files/Charizard.png').convert_alpha()
Eevee_img = pygame.image.load('img_files/eevee.jpeg').convert_alpha()
Magikarp_img = pygame.image.load('img_files/magikarp.jpeg').convert_alpha()
Pikachu_img = pygame.image.load('img_files/pikachu.jpeg').convert_alpha()
Snorlax_img = pygame.image.load('img_files/snorlax.jpeg').convert_alpha()
Squirtle_img = pygame.image.load('img_files/squirtle.jpeg').convert_alpha()

POKEMONS: dict = {0: Charizard_img, 1: Eevee_img, 2: Magikarp_img, 3: Pikachu_img, 4: Snorlax_img, 5: Squirtle_img}


class PokeGUI:
    def __init__(self, pokemon: Pokemon, img: int):
        self.pokemon: Pokemon = pokemon
        self.img = POKEMONS.get(img)

    def transform_scale(self, radius):
        return pygame.transform.scale(self.img, (radius - 10, radius - 10))


