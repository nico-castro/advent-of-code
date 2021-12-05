def parse_line(line):
    t1, t2 = line.split(' -> ')
    x1, y1 = map(int, t1.split(','))
    x2, y2 = map(int, t2.split(','))
    return x1,y1,x2,y2

def increment_map(x1: int, x2: int, y1: int, y2: int, d: {}):
    if y1 == y2:
        for x in range(min(x1,x2), max(x1,x2)+1):
            d[(x, y1)] = d.get((x, y1), 0) + 1
    elif x1 == x2:
        for y in range(min(y1,y2), max(y1,y2)+1):
            d[(x1, y)] = d.get((x1, y), 0) + 1
    else:
        for z in range(max(x1,x2) - min(x1,x2) + 1):
            # \
            if (x1 < x2 and y1 < y2) or (x2 < x1 and y2 < y1):
                x = min(x1,x2)
                y = min(y1,y2)
                d[(x+z, y+z)] = d.get((x+z, y+z), 0) + 1
            # /
            else:
                x = min(x1,x2)
                y = max(y1,y2)
                d[(x+z, y-z)] = d.get((x+z, y-z), 0) + 1

def main():
    arr = []
    with open('input.txt') as f:
        for line in f:
            arr.append(line.rstrip())
    d = {}
    for a in arr:
        x1,y1,x2,y2 = parse_line(a)
        increment_map(x1,x2,y1,y2,d)
    tot = 0
    for v in d.values():
        if v >= 2:
            tot += 1
    print(tot)

if __name__ == "__main__":
    main()

