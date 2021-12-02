#!/usr/local/bin/python3

def main():
    arr = []
    with open('input.txt') as f:
        for line in f:
            arr.append(line.rstrip())
    vert = 0
    horiz = 0
    aim = 0
    for a in arr:
        k,v = a.split(' ')
        if k == 'forward':
            horiz += int(v)
            vert += aim*int(v)
        elif k == 'down':
            aim += int(v)
        else:
            aim -= int(v)

    print(vert*horiz)
if __name__ == "__main__":
    main()

