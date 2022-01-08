"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
import random
from types import SimpleNamespace
from client import Client
from Classes import Pokemon
import json
from pygame import gfxdraw
import pygame
from pygame import *

class Button:
    def __init__(self ,x, y ,text):
        self.x =x
        self.y =y
        self.WITDH = 100
        self.HIGHT = 50
        self.color = (0,0,0)
        self.text = text

    def draw(self):
        #draw button to screen
        w, h = pygame.display.get_surface().get_size()
        pygame.draw.rect(screen,self.color,(0,h-self.HIGHT,self.WITDH,self.HIGHT),0)
        font = pygame.font.SysFont('comicsans', 12)
        text = font.render(self.text, 1, (255, 255, 255))
        screen.blit(text,(0 + (self.WITDH / 2 - text.get_width() / 2), h - (self.HIGHT / 2 + text.get_height() / 2)))

radius = 40
black = (0,0,0)
white =(255,255,255)

# init pygame
WIDTH, HEIGHT = 1080, 720

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
pygame.init()


screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
pygame.display.set_caption('Pokemon game!')
#Loading all the images
Background_img = pygame.image.load('Pokemon_Background.png')
Pokeball_img = pygame.image.load('Pokeball.png').convert_alpha()
Pokeball_img = pygame.transform.scale(Pokeball_img,(radius,radius))
Pokemon_Mester_img =pygame.image.load('Pokemon_Master.png').convert_alpha()
Pokemon_Mester_img = pygame.transform.scale(Pokemon_Mester_img,(radius-10,radius-10))

#Pokemons images
Charizard_img = pygame.image.load('Charizard.png').convert_alpha()
Charizard_img = pygame.transform.scale(Charizard_img,(radius,radius))
Eevee_img = pygame.image.load('eevee.jpeg').convert_alpha()
Eevee_img = pygame.transform.scale(Eevee_img,(radius-10,radius-10))
Magickarp_img = pygame.image.load('magikarp.jpeg').convert_alpha()
Magickarp_img = pygame.transform.scale(Magickarp_img,(radius-10,radius-10))
Pikachu_img = pygame.image.load('pikachu.jpeg').convert_alpha()
Pikachu_img = pygame.transform.scale(Pikachu_img,(radius-10,radius-10))
Snorlax_img = pygame.image.load('snorlax.jpeg').convert_alpha()
Snorlax_img = pygame.transform.scale(Snorlax_img,(radius-10,radius-10))
Squirtle_img = pygame.image.load('squirtle.jpeg').convert_alpha()
Squirtle_img = pygame.transform.scale(Squirtle_img,(radius-10,radius-10))

my_pokemons =[Charizard_img , Eevee_img ,Magickarp_img,Pikachu_img,Snorlax_img,Squirtle_img]


clock = pygame.time.Clock()
pygame.font.init()

client = Client()
client.start_connection(HOST, PORT)

pokemons = client.get_pokemons()
pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))

print(pokemons)

graph_json = client.get_graph()

FONT = pygame.font.SysFont('Arial', 20, bold=True)
# load the json string into SimpleNamespace Object

graph = json.loads(
    graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))

for n in graph.Nodes:
    x, y, _ = n.pos.split(',')
    n.pos = SimpleNamespace(x=float(x), y=float(y))

 # get data proportions
min_x = min(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
min_y = min(list(graph.Nodes), key=lambda n: n.pos.y).pos.y
max_x = max(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
max_y = max(list(graph.Nodes), key=lambda n: n.pos.y).pos.y

# Creating button instance

exit_button = Button(0, HEIGHT- 50, 'Stop')


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimentions
    """
    return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen


# decorate scale with the correct values

def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height()-50, min_y, max_y)




client.add_agent("{\"id\":0}")
client.add_agent("{\"id\":1}")
client.add_agent("{\"id\":2}")
client.add_agent("{\"id\":3}")

# this commnad starts the server - the game is running now
client.start()

"""
The code below should be improved significantly:
The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
"""

while client.is_running() == 'true':

    data = json.loads(client.get_info())["GameServer"]



    font = pygame.font.Font('freesansbold.ttf', 14)
    currTime = client.time_to_end()
    text_To_Finish = font.render('Time to finish: ' + str(int(currTime) / 1000) + ' sec.', True, black)
    textRect_To_Finish = text_To_Finish.get_rect()
    text_To_Finish.set_alpha(127)
    textRect_To_Finish.center = (90, 10)
    textRect_To_Finish.left = 5

    text_Move = font.render('Moves : ' + str(data['moves']) , True, black)
    textRect_Move = text_Move.get_rect()
    text_Move.set_alpha(127)
    textRect_Move.center = (41, 30)
    textRect_Move.left = 5

    text_OverallPoints = font.render('Total points so far : ' + str(data['grade']) , True, black)
    textRect_OverallPoints= text_OverallPoints.get_rect()
    text_OverallPoints.set_alpha(127)
    textRect_OverallPoints.center = (75, 50)
    textRect_OverallPoints.left = 5

    pokemons = json.loads(client.get_pokemons(),
                          object_hook=lambda d: SimpleNamespace(**d)).Pokemons
    pokemons = [p.Pokemon for p in pokemons]
    for p in pokemons:
        x, y, _ = p.pos.split(',')
        p.pos = SimpleNamespace(x=my_scale(
            float(x), x=True), y=my_scale(float(y), y=True))
    agents = json.loads(client.get_agents(),
                        object_hook=lambda d: SimpleNamespace(**d)).Agents
    agents = [agent.Agent for agent in agents]
    for a in agents:
        x, y, _ = a.pos.split(',')
        a.pos = SimpleNamespace(x=my_scale(
            float(x), x=True), y=my_scale(float(y), y=True))


    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


    # refresh surface
    screen.fill(Color(0, 255, 0))
    w, h = pygame.display.get_surface().get_size()
    Background_img = pygame.transform.scale(Background_img, (w, h))
    screen.blit(Background_img, [0, 0])
    screen.blit(text_To_Finish, textRect_To_Finish)
    screen.blit(text_Move, textRect_Move)
    screen.blit(text_OverallPoints, textRect_OverallPoints)

    exit_button.draw()

    # draw nodes
    for n in graph.Nodes:
        x = my_scale(n.pos.x, x=True)
        y = my_scale(n.pos.y, y=True)

        screen.blit(Pokeball_img,(int(x)-int(radius /2) ,int(y)-int(radius/2)))

        # draw the node id
        id_srf = FONT.render(str(n.id), True, Color(0, 0, 230))
        rect = id_srf.get_rect(center=(x, y - 28))
        screen.blit(id_srf, rect)

    # draw edges
    for e in graph.Edges:
        # find the edge nodes
        src = next(n for n in graph.Nodes if n.id == e.src)
        dest = next(n for n in graph.Nodes if n.id == e.dest)

        # scaled positions
        src_x = my_scale(src.pos.x, x=True)
        src_y = my_scale(src.pos.y, y=True)
        dest_x = my_scale(dest.pos.x, x=True)
        dest_y = my_scale(dest.pos.y, y=True)

        # draw the line
        pygame.draw.line(screen, Color(61, 72, 126),
                         (src_x, src_y), (dest_x, dest_y))

    # draw agents
    for agent in agents:

        screen.blit(Pokemon_Mester_img, (int(agent.pos.x) -10 , int(agent.pos.y) -10))
    # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).
    for p in pokemons:
        #cuurPokemon = random.choice(my_pokemons)
        screen.blit(Charizard_img, (int(p.pos.x) -10 , int(p.pos.y) -17))



    # update screen changes
    display.update()

    # refresh rate
    clock.tick(60)

    # choose next edge
    for agent in agents:
        if agent.dest == -1:
            next_node = (agent.src - 1) % len(graph.Nodes)
            client.choose_next_edge(
                '{"agent_id":'+str(agent.id)+', "next_node_id":'+str(next_node)+'}')
            ttl = client.time_to_end()
            print(ttl, client.get_info())

    client.move()
# game over:
