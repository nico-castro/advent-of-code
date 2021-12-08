#!/usr/local/bin/python3

def main():
    arr = []
    with open('input.txt') as f:
        for line in f:
            arr.append(line.rstrip().split(' | ')[1])

    tot = 0
    for line in arr:
        outputs = line.split(' ')
        print(outputs)
        for o in outputs:
            if len(o) == 7 or len(o) == 3 or len(o) == 2 or len(o) == 4:
                print(o)
                tot += 1
    print(tot)

if __name__ == "__main__":
    main()

