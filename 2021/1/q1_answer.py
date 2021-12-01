#!/usr/local/bin/python3

def main():
    arr = []
    with open('input.txt', 'r') as f:
        for line in f:
            arr.append(int(line.rstrip()))
    tot = 0
    for n in range(len(arr)-1):
        if arr[n] < arr[n+1]:
            tot += 1
    print(tot)

if __name__ == "__main__":
    main()

