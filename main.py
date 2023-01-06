import json
import matplotlib.pyplot as plt
import networkx as nx

from dijkstra import *

# Load the graph data from the JSON file
with open('graph1.json', encoding='utf-8-sig') as f:
    data = json.load(f)

# Creazione del grafo con Network X
G = nx.DiGraph()


for node in data['nodes']:
    G.add_node(node['id'])
for arc in data['arcs']:
    G.add_edge(arc['end1'], arc['end2'], weight=arc['weight'])
##############################################################

# Creazione del grafo da analizzare con Dijkstra
graph = {}
for node in data['nodes']:
    graph[node['id']] = {}
for arc in data['arcs']:
    graph[arc['end1']][arc['end2']] = arc['weight']


shortest_path = dijkstra(graph, 0, 5)
print(shortest_path)

# Plotting del grafo con networkx e matplot
nx.draw(G, with_labels=True)
plt.show()