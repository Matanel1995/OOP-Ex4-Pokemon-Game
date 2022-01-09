# OOP_Ex4 - Pokemon game

![Pokemon Banner](https://user-images.githubusercontent.com/92520981/148656000-f8f771b6-0acd-4469-99c0-8e37004294cd.jpg)
## Made by:
* Roey Finegold -  https://github.com/RF555 <br />
* Matanel Ohayon - https://github.com/Matanel1995 <br />
## Introduction:          
In this assignment we implemented a Pokemon game based on the previous assignments we had in this course.</br>
In this game there are 16 cases witch the user can choose.
the cases are differ by:
* number of agents.
* number of Pokemons.
* different graph.
</br>
The goal is to collect as many Pokemons within the given time , and do not exceed 10 moves per second. </br>


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

## Gready but smart
In order to decided how to allocate agent to each Pokemon we used gready algorithm.</br>
That mean that we allocate to each agent his "best" pokemon.</br>
The way we choose the "best" pokemon for each agent is by the Pokemon value/Time to rach him, that done at the **value_per_time** function</br>
in that way we make sure each agent will choose a Pokemon that will maximise our total points.</br>

## UML
![UML](https://user-images.githubusercontent.com/92520981/148657249-f2a48245-f3d3-4af0-85a8-a69287696615.jpeg)</br>


## Previous project
All the function we used that related to the graph such as 
* Shortest path
* Initialize graph
* And more
can be found here with more explanation : [Ex3-OOP-Graph](https://github.com/RF555/OOP_Ex3)<br/>

## Glimpse at the game </br>

![GUI](https://user-images.githubusercontent.com/76430709/148659372-9bbb97e1-31cb-40f0-8148-a1e75abdf52e.jpg)</br>

### Video of case 11
You can watch it here [YouTube](https://www.youtube.com/watch?v=NO44NKtqArc)</br>


## How to run:
* Clone the repository from this github 
* Open CMD in the project directory
* Run this function
* >pyhon3 Ex4.py
* After that you will be rquired to insert case number , choose between 0 to 15 and press Enter
![RunCMD](https://user-images.githubusercontent.com/92520981/148658653-4a375c93-5a26-49ad-ad73-d2b743841139.jpeg)
