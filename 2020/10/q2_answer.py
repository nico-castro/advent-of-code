#!/usr/local/bin/python3

def create_graph(joltages: []) -> {}:
    graph = {}
    for j in range(len(joltages) - 1):
        neighbors = []
        i = j + 1
        while i < len(joltages):
            if joltages[i] <= joltages[j] + 3:
                neighbors.append(joltages[i])
            else:
                break
            i = i + 1
        graph[joltages[j]] = neighbors
    graph[joltages[-1]] = []
    return graph

def parse_and_sort(name: str) -> []:
    jolts = [0, ]
    with open(name, 'r') as f:
        for line in f:
            jolts.append(int(line.rstrip()))
    jolts.sort()
    jolts.append(jolts[-1] + 3)
    return jolts

def traverse_graph(graph: {}, v: int, end: int, mem={}):
    if v in mem:
        return mem[v]
    elif v == end:
        return 1    
    else:
        mem[v] = sum(traverse_graph(graph, j, end, mem) for j in graph[v])
        return mem[v]

def main():
    joltages = parse_and_sort('input.txt')
    graph = create_graph(joltages)

    total = traverse_graph(graph, joltages[0], joltages[-1])
    print(total)

if __name__ == "__main__":
    main()

