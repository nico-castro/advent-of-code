#!/usr/local/bin/python3
import sys
def total_fuel_cost(crabs: [], pos: int) -> int:
    return sum(map(lambda c : abs(pos - c), crabs))

def main():
    with open('input.txt') as f:
        crabs = list(map(int, f.readline().rstrip().split(',')))

    min_cost = sys.maxsize
    for pos in crabs:
        cost = total_fuel_cost(crabs, pos)
        if cost < min_cost:
            min_cost = cost
    print(min_cost)

if __name__ == "__main__":
    main()

