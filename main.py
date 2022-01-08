import json
import os
from Classes.Pokemon import *


def init_pokemons(pokemons):
    pokemon_obj = json.loads(pokemons)

    for p in pokemon_obj['Pokemons']:
        print(p)
        temp = Pokemon(p['Pokemon'])


if __name__ == '__main__':
    i0 = ' 0'
    os.system('java -jar Ex4_Server_v0.0.jar' + i0)
    # os.system('java -jar Ex4_Server_v0.0.jar 11')
    # p1 = Pokemon(1, 1, 1, 1, 1)
    # print(p1)
    # p2 = Pokemon(2, 2, 2, 2, 2)
    # print(p2)
    # p3 = Pokemon(3, 3, 3, 3, 3)
    # print(p3)
    # p4 = Pokemon(4, 4, 4, 4, 4)
    # print(p4)
    # p5 = Pokemon(5, 5, 5, 5, 5)
    # print(p5)
