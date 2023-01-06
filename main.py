import json
import networkx as nx
import matplotlib.pyplot as plt
from dijkstra import *

# Lettura del grafo da file JSON

with open('graph1.json', encoding='utf-8-sig') as f:
    data = json.load(f)

# Creazione del grafo
G = nx.DiGraph()
for node in data['nodes']:
    G.add_node(node['id'], label=node['label'])
for arc in data['arcs']:
    G.add_edge(arc['end1'], arc['end2'], weight=arc['weight'])

# Esecuzione dell'algoritmo di Dijkstra
path = dijkstra(G, 0, 5)
print(path)

# Disegno del grafo
pos = nx.spring_layout(G)
nx.draw(G, pos=pos, with_labels=True)

# Creazione del percorso ottenuto con l'algoritmo di Dijkstra
path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]

# Disegno del percorso
nx.draw_networkx_edges(G, pos=pos, edgelist=path_edges, width=8, edge_color='r')

plt.show()