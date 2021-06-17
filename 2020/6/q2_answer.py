#!/usr/local/bin/python3

def group_sum(group: []) -> int:
    hmap = {}
    total = 0
    group_len = len(group)
    for person in group:
        for answer in person:
            hmap[answer] = hmap.get(answer, 0) + 1
    
    for question in hmap:
        if hmap[question] == group_len:
            total = total + 1
    return total

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

