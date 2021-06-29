#!/usr/local/bin/python3

def group_sum(group: []) -> int:
    hmap = {}
    for person in group:
        for answer in person:
            hmap[answer] = 1
    return len(hmap)

def main():
    total = 0
    with open('input.txt', 'r') as f:
      group = []
      for line in f:
          if line == "\n":
            total = total + group_sum(group)
            group = []
            continue
          else:
            group.append(line.rstrip())

    print(total)

if __name__ == "__main__":
    main()

