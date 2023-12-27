import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations
import json

class Graph:

    def __init__(self):
        self.graph = nx.Graph()

    def run(self):
        file = open('graphs/graph1.json')
        graph_data = json.load(file)

        for key in graph_data.keys():
            current_vertex = int(key)
            vertex_connections = graph_data[key]

            for connection_key in vertex_connections:
                connection_value = int(connection_key)
                connection_edge = int(vertex_connections[connection_key])
                
                self.graph.add_edge(current_vertex, connection_value, weight=connection_edge)

        path = self.get_best_path()

        print(f"-> Menor caminho encontrado: {path}")

        self.show_graph(path)

    def get_best_path(self):
        start = 1
        end = 3

        return nx.shortest_path(self.graph, source=start, target=end)

    def show_graph(self, path=None):
        positions = nx.fruchterman_reingold_layout(self.graph)
        nx.draw(self.graph, positions, with_labels=True, font_weight='bold', node_size=700, node_color='lightgreen')

        if path:
            edges_path = [(path[x], path[x+1]) for x in range(len(path)-1)]
            nx.draw_networkx_edges(self.graph, positions, edgelist=edges_path, edge_color='red', width=2)

        labels = {(x, y): self.graph[x][y]['weight'] for x, y in self.graph.edges()}
        nx.draw_networkx_edge_labels(self.graph, positions, edge_labels=labels)

        plt.show()

graph = Graph()
graph.run()


