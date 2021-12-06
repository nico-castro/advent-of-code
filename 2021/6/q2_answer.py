#!/usr/local/bin/python3
"""
After 7 days, the initial fish will have produced some constant set of fish.
That constant set will produce another constant after 7 days... and so on.

We want to only store the new set of fish that is produced after 7 days and figure out what it will produce after 7 days
"""
def add_day(school):
    spawn = school[0]
    for age in range(8):
        school[age] = school[age+1]
    school[6] += spawn
    school[8] = spawn

def main():
    with open('input.txt') as f:
        for line in f:
            fish = list(map(int, line.rstrip().split(',')))
    school = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for f in fish:
        school[f] += 1

    for d in range(256):
        add_day(school)
    print(school)
    print(sum(school.values()))

if __name__ == "__main__":
    main()

