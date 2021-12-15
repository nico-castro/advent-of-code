#!/usr/local/bin/python3
import sys


def minDistance(graph, dist, sptSet):
        # Initialize minimum distance for next node
        _min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for r in range(len(graph)):
            for c in range(len(graph)):
                if dist[r][c] < _min and (r, c) not in sptSet:
                    _min = dist[r][c]
                    min_index = (r, c)

        return min_index


def dijkstra(graph):
    dist = [[sys.maxsize]*len(graph) for _ in range(len(graph))]
    dist[0][0] = 0
    sptSet = {}  # {tuple: int} representing the x,y coords -> the cost of getting to it

    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(sptSet) < len(graph)**2:
        r, c = minDistance(graph, dist, sptSet)

        sptSet[(r, c)] = graph[r][c]

        for x, y in neighbors:
            if 0 <= r+x < len(graph) and 0 <= c+y < len(graph):
                if dist[r][c] + graph[r+x][c+y] < dist[r+x][c+y]:
                    dist[r+x][c+y] = dist[r][c] + graph[r+x][c+y]

    return dist


def expand_graph(graph):
    L = len(graph)
    X = 5
    expanded = [[0]*L*X for _ in range(L*X)]

    for r in range(L*X):
        for c in range(L*X):
                expanded[r][c] = (graph[r % L][c % L] + r//L + c//L - 1) % 9 + 1
    return expanded


def main():
    graph = []
    with open('input.txt') as f:
        for line in f:
            graph.append(list(map(int, list(line.rstrip()))))

    expanded = expand_graph(graph)

    print(dijkstra(expanded)[-1][-1])


if __name__ == "__main__":
    main()
