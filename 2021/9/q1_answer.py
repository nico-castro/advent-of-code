#!/usr/local/bin/python3

def main():
    arr = []
    with open('input.txt') as f:
        for line in f:
            arr.append(list(line.rstrip()))

    tot = 0
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if r > 0 and arr[r][c] >= arr[r-1][c]:
                # check up
                continue
            if r < len(arr) - 1 and arr[r][c] >= arr[r+1][c]:
                # check down
                continue
            if c > 0 and arr[r][c] >= arr[r][c-1]:
                # check left
                continue
            if c < len(arr[r]) - 1 and arr[r][c] >= arr[r][c+1]:
                # check right
                continue
            tot += 1 + int(arr[r][c])
    print(tot)

if __name__ == "__main__":
    main()

