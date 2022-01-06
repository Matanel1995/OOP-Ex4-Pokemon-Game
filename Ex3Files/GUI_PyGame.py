import math
import sys

import pygame
from pygame import QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN

# from src import GraphAlgoInterface, GraphAlgo
from DiGraph import *

pygame.init()
# init display res
infoObject = pygame.display.Info()
# pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
screen_res = (infoObject.current_w, infoObject.current_h)
display_width = max(1000, int(2 * screen_res[0] / 3))
display_height = max(600, int(2 * screen_res[1] / 3))

clock = pygame.time.Clock()
# graphDisplay = pygame.display.set_mode((display_width, display_height))
graphDisplay = pygame.display.set_mode(screen_res)
pygame.display.set_caption('Ex3')

# Parameters
# GRAPH =

# Colors:
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (127, 0, 255)
pink = (255, 0, 255)
orange = (255, 128, 0)
light_red = (255, 153, 153)
light_green = (153, 255, 153)
light_blue = (153, 204, 255)
light_yellow = (255, 255, 153)
light_purple = (204, 153, 255)
light_pink = (255, 204, 255)
light_orange = (255, 204, 153)
light_grey = (192, 192, 192)
dark_red = (102, 0, 0)
dark_green = (0, 102, 0)
dark_blue = (0, 0, 102)
dark_purple = (51, 0, 102)

corbel = pygame.font.SysFont('Corbel', 35)
calibri = pygame.font.SysFont('Calibri', 35)
ariel_node = pygame.font.SysFont('Ariel', 35)
ariel_edge = pygame.font.SysFont('Ariel', 15)


def draw_text(text, font, color, surface, x, y):
    text_st = font.render(text, 1, color)
    text_rect = text_st.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_st, text_rect)


def plot_graph(my_graph: DiGraph):
    global click
    while True:
        graphDisplay.fill(white)

        # pygame.draw.circle(graphDisplay, light_purple, (display_width, display_height), 30)
        # pygame.draw.circle(graphDisplay, light_purple, (0, 0), 30)
        #
        # draw_text('main menu', ariel_node, (255, 255, 255), graphDisplay, 20, 20)

        max_x = 0
        max_y = 0
        min_x = MAX_FLOAT
        min_y = MAX_FLOAT
        for node in my_graph.nodes.values():
            max_x = max(max_x, node.pos[0])
            max_y = max(max_y, node.pos[1])
            min_x = min(min_x, node.pos[0])
            min_y = min(min_y, node.pos[1])

        min_max = (max_x, min_x, max_y, min_y)
        if my_graph.v_size() == 0:
            radius = 20
        else:
            radius = max(display_width / my_graph.v_size() / 20, 15)
        gen_nodes(my_graph.nodes, radius, min_max)
        gen_edges(my_graph, radius, min_max)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


def for_quit():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


def gen_nodes(_nodes: dict[Node], radius: float, min_max: tuple):
    for node in _nodes.values():
        curr_x = node.pos[0]
        curr_y = node.pos[1]
        x_coo = scale_x(curr_x, min_max)
        y_coo = scale_y(curr_y, min_max)
        pygame.draw.circle(graphDisplay, orange, (x_coo, y_coo), radius)
        pygame.draw.circle(graphDisplay, dark_green, (x_coo, y_coo), radius - 4)
        draw_text(f"{node.id}", ariel_node, GREY, graphDisplay, x_coo - radius / 2, y_coo - radius / 2)
    # pygame.display.update()
    # clock.tick(60)


def draw_arrow(colour, src_x, src_y, dest_x, dest_y, w):
    pygame.draw.line(graphDisplay, colour, (src_x, src_y), (dest_x, dest_y), 2)
    draw_tip((src_x, src_y), (dest_x, dest_y), colour)


def draw_curved_arrow(colour, src_x, src_y, dest_x, dest_y, w):
    top = min(src_x, dest_x)
    left = min(src_y, dest_y)
    bottom = max(src_x, dest_x)
    right = max(src_y, dest_y)
    height = bottom - top
    length = right - left
    rect = pygame.Rect((top, left), (length, height))
    pygame.draw.arc(graphDisplay, colour, rect, math.pi / 2, math.pi / 2, 2)
    draw_tip((src_x, src_y), (dest_x, dest_y), pink)


def draw_tip(start, end, color):
    rotation = math.degrees(math.atan2(start[1] - end[1], end[0] - start[0])) + 90
    pygame.draw.polygon(graphDisplay, color, (
        (end[0] + 10 * math.sin(math.radians(rotation)), end[1] + 10 * math.cos(math.radians(rotation))),
        (end[0] + 10 * math.sin(math.radians(rotation - 120)), end[1] + 10 * math.cos(math.radians(rotation - 120))),
        (end[0] + 10 * math.sin(math.radians(rotation + 120)), end[1] + 10 * math.cos(math.radians(rotation + 120)))))


def gen_edges(my_graph: DiGraph, radius, min_max: tuple):
    edge_check = my_graph.edges.copy()
    for src_id, src_node in my_graph.nodes.items():
        for dest_id, w in src_node.edges_out.items():
            src_x = scale_x(src_node.pos[0], min_max)
            src_y = scale_y(src_node.pos[1], min_max)
            dest_x = scale_x(my_graph.nodes.get(dest_id).pos[0], min_max)
            dest_y = scale_y(my_graph.nodes.get(dest_id).pos[1], min_max)

            # temp_src_x = scale_x(src_node.pos[0], min_max)
            # temp_src_y = scale_y(src_node.pos[1], min_max)
            # temp_dest_x = scale_x(my_graph.nodes.get(dest_id).pos[0], min_max)
            # temp_dest_y = scale_y(my_graph.nodes.get(dest_id).pos[1], min_max)
            # if temp_src_x >= temp_dest_x:
            #     src_x = temp_src_x - radius/2
            #     dest_x = temp_dest_x + radius/2
            # else:  # temp_src_x < temp_dest_x:
            #     src_x = temp_src_x + radius/2
            #     dest_x = temp_dest_x - radius/2
            # if temp_src_y >= temp_dest_y:
            #     src_y = temp_src_y - radius/2
            #     dest_y = temp_dest_y + radius/2
            # else:  # temp_src_y < temp_dest_y:
            #     src_y = temp_src_y + radius/2
            #     dest_y = temp_dest_y - radius/2

            # draw_curved_arrow(black, src_x, src_y, dest_x, dest_y, w)
            # draw_arrow(black, src_x, src_y, dest_x, dest_y, w)
            if dest_id in src_node.edges_in.keys():
                if edge_check[st_edge(dest_id, src_id)] != -1:
                    # pygame.draw.line(graphDisplay, pink, (src_x, src_y + radius), (dest_x, dest_y + radius), 5)
                    # draw_tip((src_x, src_y + radius), (dest_x, dest_y + radius), pink)
                    pygame.draw.line(graphDisplay, pink, (src_x + radius, src_y + radius),
                                     (dest_x + radius, dest_y + radius), 5)
                    draw_tip((src_x + radius, src_y + radius), (dest_x + radius, dest_y + radius), pink)
                    draw_text(f'{w}', ariel_edge, pink, graphDisplay, abs(src_x + dest_x + 3 * radius) / 2,
                              abs(src_y + dest_y + 3 * radius) / 2)
                    edge_check[st_edge(src_id, dest_id)] = -1
                else:
                    # pygame.draw.line(graphDisplay, light_pink, (src_x, src_y - radius), (dest_x, dest_y - radius), 5)
                    # draw_tip((src_x, src_y - radius), (dest_x, dest_y - radius), light_pink)
                    pygame.draw.line(graphDisplay, light_pink, (src_x- radius, src_y - radius), (dest_x- radius, dest_y - radius), 5)
                    draw_tip((src_x- radius, src_y - radius), (dest_x- radius, dest_y - radius), light_pink)
                    draw_text(f'{w}', ariel_edge, light_pink, graphDisplay, abs(src_x + dest_x - 4 * radius) / 2,
                              abs(src_y + dest_y - 4 * radius) / 2)
                    edge_check[st_edge(src_id, dest_id)] = -1
            else:
                pygame.draw.line(graphDisplay, pink, (src_x, src_y + radius), (dest_x, dest_y + radius), 5)
                draw_tip((src_x, src_y + radius), (dest_x, dest_y + radius), pink)
                draw_text(f'{w}', ariel_edge, pink, graphDisplay, abs(src_x + dest_x + 3*radius) / 2,
                          abs(src_y + dest_y + 3*radius) / 2)
                edge_check[st_edge(src_id, dest_id)] = -1


def scale_x(x_coo, min_max: tuple):
    return (display_width - 100) * (x_coo - min_max[1]) / (min_max[0] - min_max[1]) + 20


def scale_y(y_coo, min_max: tuple):
    return (display_height - 100) * (y_coo - min_max[3]) / (min_max[2] - min_max[3]) + 20
