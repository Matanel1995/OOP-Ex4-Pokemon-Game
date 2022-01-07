# default port
from client import Client

PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'

client = Client()
client.start_connection(HOST, PORT)
graph_json = client.get_graph()

def game_client():
