#!/usr/local/bin/python3

def parse_and_sort(name: str) -> []:
    jolts = [0, ]
    with open(name, 'r') as f:
        for line in f:
            jolts.append(int(line.rstrip()))
    jolts.sort()
    jolts.append(jolts[-1] + 3)
    return jolts

def main():
    joltages = parse_and_sort('input.txt')
    jumps = {}

    for i in range(len(joltages)-1):
        jump = joltages[i+1] - joltages[i]
        jumps[jump] = jumps.get(jump, 0) + 1
    
    print(jumps[1] * jumps[3])

if __name__ == "__main__":
    main()

