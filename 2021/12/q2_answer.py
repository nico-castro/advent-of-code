#!/usr/local/bin/python3
from collections import defaultdict


def valid_next_nodes(graph: {str: set}, node: str, visited_small: set,
                     small_dupe: tuple) -> [str]:
    """
    Inputs:
        graph:          dictionary of nodes -> set(connected nodes)
        node:           str representing current node
        visited_small:  set of nodes that represent small caves that have
                        been visited
        small_dupe:     tuple(str, bool) (small cave that can be visited twice,
                        has it been visited once yet)
    Output:
        The list of valid nodes to visit next.
    """
    return [n for n in graph[node] if n not in visited_small or (n == small_dupe[0] and small_dupe[1] < 2)]


def find_all_paths(graph: {str: set}, node: str, visited_small: set, path: [str],
                   all_paths: set, small_dupe: tuple):
        if node.islower():
            visited_small.add(node)
        if node == small_dupe[0]:
            small_dupe = (small_dupe[0], small_dupe[1]+1)
        path.append(node)

        if node == 'end':
            all_paths.add(','.join(path))
        else:
            for n in valid_next_nodes(graph, node, visited_small, small_dupe):
                find_all_paths(graph, n, visited_small, path, all_paths, small_dupe)

        path.pop()
        if node.islower():
            if node == small_dupe[0]:
                small_dupe = (small_dupe[0], small_dupe[1]-1)
            else:
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

    all_paths = set()

    for small in [n for n in caves if n.islower() and n not in {'start', 'end'}]:
        find_all_paths(caves, 'start', set(), [], all_paths, (small, 0))

    print(len(all_paths))


if __name__ == "__main__":
    main()
