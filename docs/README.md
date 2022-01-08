# OOP_Ex4 - Pokemon game

![Pokemon Banner](https://user-images.githubusercontent.com/92520981/148656000-f8f771b6-0acd-4469-99c0-8e37004294cd.jpg)
## Made by:
* Roey Finegold -  https://github.com/RF555 <br />
* Matanel Ohayon - https://github.com/Matanel1995 <br />
## Introduction:          
In this assiment we implemneted a Pokemon game based on the previus assingments we had in this course.</br>
In this game there are 16 cases witch the user can choose.
ther cases are deffer by:
* number of agents.
* number of Pokemons.
* different graph.
The goal is to collect as many Pokemons whitin the given time , and do not exeed 10 moves per second. </br>


## Main functions
### GameAlgo:
| Function name | Explanation |
| ------------- | ------------- |
| __init__(self) | initialize the game | 
| update_game(self, pokemons = None , agents = None, graph =None) | initialize the game with the given parameters|
| allocate_all_agents(self) | Allocate for each agent a Pokemon to catch |
| value_per_time(self , a:Agent) | Choose for each agent the best Pokemon for him  as function of value/time to reach|
| time_to_poke(self, agent_id: int, poke_src: int) -> float | Calculate the time for an agent to reach specific Pokemon |
| find_pok_src_dst(self , pokemon :Pokemon) | Find on which edge this Pokemon is on |
| find_dist_nodes(self,node1 : Node , node2 :Node) | Calculate distance between 2 nodes |
| all_pok_src_dst(self) | Uses find_pok_src_dst to find all Pokemons edges and update the Pokemon object acordelly |
| CMD(self,Client:Client) | Check if it possible to send an agent to catch Pokemon if so send him|
| begining_of_the_game(self, Client:Client) | Initialize what requierd for the game  |
| game_algorithm(self,Client:Client) | Run all the required function for the game to run | 


### GameGUI:
| Function name | Explanation |
| ------------- | ------------- |
| __init__(self, game) | initialize the GUI |
| init_screen(self) | Initilize all the object needed to be shown in the screen |
| update_gui(self,game:GameAlgo ,Client:Client) | Update the Pokemon and agents as the game run |
| draw_nodes(self): | Draw on the screen all the nodes |
| draw_edegs(self) | Draw on the screen all the edges |
| draw_agent(self) | Draw on the screen all the agents |
| draw_pokemon(self) | Draw on the screen all the Pokemons |
| scale(self, data, min_screen, max_screen, min_data, max_data) | Scale the possition of object to Pixels value |
| def my_scale(self,data, x=False, y=False) | Scale the possition of object to Pixels value |
</br>

## Glimps at the game. </br>

![GUI](https://user-images.githubusercontent.com/92520981/148656038-2a4c3401-5eab-4f0d-8cdd-070f9b909ae3.png)</br>

## How to run:
to use the jar file use command (0 &le; i &le; 15):

java -jar Ex4_Server_v0.0.jar i

