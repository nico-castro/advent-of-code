#!/usr/local/bin/python3
from collections import Counter


def insert(polymer: [str], rules: {}) -> str:
    new_polymer = ''
    for i in range(len(polymer)-1):
        new_polymer += polymer[i] + rules[polymer[i]+polymer[i+1]]
    new_polymer += polymer[-1]
    return new_polymer


def main():
    rules = {}
    with open('input.txt') as f:
        template = f.readline().rstrip()
        for line in f:
            if line != '\n':
                pair, ins = line.rstrip().split(' -> ')
                rules[pair] = ins

    polymer = template
    for _ in range(40):
        polymer = insert(polymer, rules)

    count = Counter(polymer)
    print(max(count.values()) - min(count.values()))


if __name__ == "__main__":
    main()
