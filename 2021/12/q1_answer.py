#!/usr/local/bin/python3
from collections import defaultdict


def valid_next_nodes(graph: {set}, node: str, visited_small: set) -> [str]:
    return [n for n in graph[node] if n not in visited_small]


def find_all_paths(graph: {set}, node: str, visited_small: set, path: [str], all_paths: [[str]]):
        if not node.isupper():
            visited_small.add(node)
        path.append(node)

        if node == 'end':
            all_paths.append(path.copy())
        else:
            for n in valid_next_nodes(graph, node, visited_small):
                if n not in visited_small:
                    find_all_paths(graph, n, visited_small, path, all_paths)

        path.pop()
        if not node.isupper():
            visited_small.remove(node)


def main():
    caves = defaultdict(set)
    arr = []
    with open('input.txt') as f:
        for line in f:
            arr.append(tuple(line.rstrip().split('-')))

    for v1, v2 in arr:
        caves[v1].add(v2)
        caves[v2].add(v1)

    visited_small = set()
    all_paths = []

    find_all_paths(caves, 'start', visited_small, [], all_paths)
    print(len(all_paths))


if __name__ == "__main__":
    main()
