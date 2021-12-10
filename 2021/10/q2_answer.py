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
    if c == '(':
        return ')'
    if c == '[':
        return ']'
    if c == '{':
        return '}'
    if c == '<':
        return '>'


def points(c):
    if c == ')':
        return 1
    if c == ']':
        return 2
    if c == '}':
        return 3
    if c == '>':
        return 4


def generate_closes(line: str):
    opens = deque()
    for c in list(line): 
        if c in ['(', '[', '{', '<']:
            opens.append(c)
        else:
            if opens.pop() != pair(c):
                return None
    closes = []
    while len(opens):
        closes.append(pair(opens.pop()))
    return ''.join(closes)


def main():
    arr = []
    with open('input.txt') as f:
        for line in f:
            arr.append(line.rstrip())

    scores = []
    for l in arr:
        tot = 0
        closes = generate_closes(l)
        if not closes:
            continue
        for c in list(closes):
             tot = tot*5 + points(c) 
        scores.append(tot)
    print(sorted(scores)[len(scores)//2])

if __name__ == "__main__":
    main()

