#!/usr/local/bin/python3

def main():
    arr = []
    with open('input.txt') as f:
        for line in f:
            arr.append(line.rstrip())
    vert = 0
    horiz = 0
    for a in arr:
        k,v = a.split(' ')
        if k == 'forward':
            horiz += int(v)
        elif k == 'down':
            vert += int(v)
        else:
            vert -= int(v)

    print(vert*horiz)
if __name__ == "__main__":
    main()

