#!/usr/local/bin/python3
import sys
def total_fuel_cost(crabs: [], pos: int) -> int:
    return sum(map(lambda c : sum(range(abs(pos - c)+1)), crabs))

def main():
    with open('input.txt') as f:
        crabs = list(map(int, f.readline().rstrip().split(',')))

    min_cost = sys.maxsize
    pos = min(crabs)
    cost = total_fuel_cost(crabs, pos)
    while cost < min_cost:
        min_cost = cost
        pos += 1
        cost = total_fuel_cost(crabs, pos)

    print(min_cost, pos)

if __name__ == "__main__":
    main()

