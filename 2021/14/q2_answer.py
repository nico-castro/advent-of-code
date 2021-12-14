#!/usr/local/bin/python3
from collections import Counter


def create_first_pairs(template: str) -> {str: int}:
    pairs = {}
    for i in range(len(template)-1):
        p = template[i]+template[i+1]
        pairs[p] = pairs.get(p, 0) + 1
    return pairs


def generate_next_pairs(pairs: {str: int}, rules: {str: str}) -> {str: int}:
    new_pairs = {}
    for k, v in pairs.items():
        next_1 = k[0]+rules[k]
        next_2 = rules[k]+k[1]
        new_pairs[next_1] = new_pairs.get(next_1, 0) + v
        new_pairs[next_2] = new_pairs.get(next_2, 0) + v
    return new_pairs


def count_pairs(pairs: {str: int}, template: str) -> {str: int}:
    c = Counter([template[0], template[-1]])
    for k, v in pairs.items():
        c[k[0]] += v
        c[k[1]] += v
    return c


def main():
    rules = {}
    with open('input.txt') as f:
        template = f.readline().rstrip()
        for line in f:
            if line != '\n':
                pair, ins = line.rstrip().split(' -> ')
                rules[pair] = ins

    pairs = create_first_pairs(template)

    for _ in range(40):
        pairs = generate_next_pairs(pairs, rules)

    count = count_pairs(pairs, template)

    print((max(count.values()) - min(count.values()))//2)


if __name__ == "__main__":
    main()
