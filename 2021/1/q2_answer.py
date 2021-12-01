#!/usr/local/bin/python3

def main():
    arr = []
    with open('input.txt', 'r') as f:
        for line in f:
            arr.append(int(line.rstrip()))

    tot = 0
    prev_window = 1000000000

    for n in range(len(arr)-2):
        window = sum(arr[n:n+3])
#        print(window, prev_window)
        if window > prev_window:
            tot += 1
        prev_window = window
    print(tot)

if __name__ == "__main__":
    main()

