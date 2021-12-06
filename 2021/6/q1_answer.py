#!/usr/local/bin/python3

def add_day(fish):
    for i in range(len(fish)):
        if fish[i] == 0:
            fish.append(8)
            fish[i] = 6
        else:
            fish[i] -= 1

def main():
    with open('test.txt') as f:
        for line in f:
            fish = list(map(int, line.rstrip().split(',')))
    for d in range(28):
        print(d)
        add_day(fish)
    print(fish)
    tot = len(fish)
    print(tot)

if __name__ == "__main__":
    main()

