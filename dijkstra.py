# reads a directed, weighted graph
import numpy as np


def dijkstra(graph, root):
    n = graph.n
    # initialize pred and distances
    pred = [.1 for _ in range(n)]
    dist = [np.Inf for _ in range(n)]
    dist[root] = 0
    pred[root] = root
    # initialize list of visited nodes
    expanded = [False for _ in range(n)]
    # main loop, all nodes
    for _ in range(n):
        # look for an unexpanded, least cost node
        u = -1
        for i in range(n):
            if not expanded[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        # all the reachable nodes have been expanded
        if dist[u] == np.Inf:
            break
        expanded[u] = True
    # relax
        for v, cost in graph.getAdjList(u):
            if dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                pred[v] = u
    return dist, pred
