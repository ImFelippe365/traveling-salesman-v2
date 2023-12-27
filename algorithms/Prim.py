import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations
import json

class Graph:

    def __init__(self):
        self.graph = nx.Graph()

    def run(self):
        file = open('graphs/graph2.json')
        graph_data = json.load(file)

        for key in graph_data.keys():
            current_vertex = int(key)
            vertex_connections = graph_data[key]

            for connection_key in vertex_connections:
                connection_value = int(connection_key)
                connection_edge = int(vertex_connections[connection_key])
                
                self.graph.add_edge(current_vertex, connection_value, weight=connection_edge)

        best_path, path_length = self.get_best_path()

        print(f"-> Menor caminho encontrado: {best_path}")
        print(f"-> Tamanho do caminho: {path_length}")

        self.show_graph(best_path)

    def get_best_path(self):
        arvore_prim = nx.minimum_spanning_tree(self.graph, algorithm='prim', weight='weight')
        
        caminho_tsp = list(nx.dfs_preorder_nodes(arvore_prim, source=1))
        caminho_tsp.append(caminho_tsp[0])
        comprimento_tsp = 0

        for i in range(len(caminho_tsp)-1):
            origem = caminho_tsp[i]
            destino = caminho_tsp[i+1]

            if self.graph.has_edge(origem, destino):
                comprimento_tsp += self.graph[origem][destino]['weight']

        return caminho_tsp, comprimento_tsp

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


