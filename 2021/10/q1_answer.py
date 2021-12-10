#!/usr/local/bin/python3
from collections import deque

def pair(c):
    if c == ')':
        return '('
    if c == ']':
        return '['
    if c == '}':
        return '{'
    if c == '>':
        return '<'

def points(c):
    if c == ')':
        return 3
    if c == ']':
        return 57
    if c == '}':
        return 1197
    if c == '>':
        return 25137



def find_first_illegal(line: str):
    opens = deque()
    for c in list(line):
        if c in ['(', '[', '{', '<']:
            opens.append(c)
        else:
            if opens.pop() != pair(c):
                return c


def main():
    arr = []
    with open('input.txt') as f:
        for line in f:
            arr.append(line.rstrip())
    tot = 0
    for l in arr:
        char = find_first_illegal(l)
        if char:
            tot += points(char)
    print(tot)


if __name__ == "__main__":
    main()

