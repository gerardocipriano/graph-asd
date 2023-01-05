import os
import json  # standard library no need to install


import Graph  # weighted graph
from dijkstra import *

import igraph as ig
import matplotlib.pyplot as plt


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open('graph1.json', encoding='utf-8-sig') as jfile:
        jgraph = json.load(jfile)
    print(jgraph['name'])
    G = Graph.Graph(isDirected=jgraph['isDirected'])
    for n in jgraph['nodes']:
        G.addNode(n)
    for m in jgraph['arcs']:
        G.addEdge(m['end1'], m['end2'], (m['weight'] if "weight" in m.keys() else 1))

    g = ig.Graph(directed=True)
    g.add_vertices(6)
    g.add_edges([(0, 1), (1, 0), (0, 2),(1, 2), (2, 1), (1, 3),(3, 2), (2, 3), (2, 4), (4, 2),(3, 5), (4, 3), (5, 4)])
    # Generate the graph with its capacities
    g.vs["name"] = ["s", "v1", "v2", "v3", "v4", "t"]
    g.es["weight"] = [12, 4, 13, 10, 4, 8, 5, 4, 10, 4, 20, 7, 4]  # weight of each edge
    g.es["capacity"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # capacity of each edge
    g.es["width"] = [3, 1, 1, 3, 1, 1, 1, 1, 3, 1, 3, 3, 1]  # drawing width of each edge
    g.es["color"] = ['#F00', '#666', '#666', '#F00', '#666', '#666', '#666', '#666', '#F00',
                     '#666', '#F00', '#F00', '#666']
    grid = [[0, 2], [2, 4], [2, 0], [4, 4], [4, 0], [6, 2]]

    G.printAdjlists()
    print(dijkstra(G, 0))

    fig, ax = plt.subplots()
    ig.plot(
        g,
        target=ax,
        layout=grid,
        vertex_size=0.5,
        vertex_color='lightblue',
        vertex_label=g.vs['name'],
        edge_width=g.es['width'],
        edge_label=g.es["weight"],
        edge_color=g.es["color"],
        edge_align_label=True,
        edge_background='white'
    )
    plt.show()


