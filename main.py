import json
import matplotlib.pyplot as plt
import networkx as nx

# Load the graph data from the JSON file
with open('graph1.json', encoding='utf-8-sig') as f:
    data = json.load(f)

# Create a directed, weighted graph using the NetworkX library
G = nx.DiGraph()


for node in data['nodes']:
    G.add_node(node['id'])
for arc in data['arcs']:
    G.add_edge(arc['end1'], arc['end2'], weight=arc['weight'])


shortest_path = nx.dijkstra_path(G, 0, 5)


print(shortest_path)


nx.draw(G, with_labels=True)
plt.show()