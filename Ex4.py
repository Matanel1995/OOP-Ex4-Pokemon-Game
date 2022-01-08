from time import sleep
import GameGUI as GameGUI
from pygame import *
import GameAlgo as GameAlgo
from client import Client


def main():
    PORT = 6666
    # server host (default localhost 127.0.0.1)
    HOST = '127.0.0.1'
    MyClient = Client()
    MyClient.start_connection(HOST, PORT)
    game = GameAlgo.GameAlgo()
    game.begining_of_the_game(MyClient)
    game.update_game(MyClient.get_pokemons(), MyClient.get_agents(), MyClient.get_graph())
    gui = GameGUI.GameGui(game)
    gui.init_screen()
    MyClient.start()
    while MyClient.is_running() == "true":
        game.update_game(MyClient.get_pokemons(), MyClient.get_agents())
        gui.update_gui(game, MyClient)
        game.game_algorithm(MyClient)
        print(MyClient.time_to_end())
        print(MyClient.get_pokemons())
        print(MyClient.get_info())
        sleep(0.05)
    MyClient.stop_connection()
    exit(0)


if __name__ == "__main__":
    main()
