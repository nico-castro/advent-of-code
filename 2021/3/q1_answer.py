#!/usr/local/bin/python3

def main():
    arr = []
    with open('input.txt') as f:
        for line in f:
            arr.append(line.rstrip())
    g = [0]*len(arr[0])
    for s in arr:
        for i, c in enumerate(s):
            if c == '1':
                g[i] += 1
    gam = ''
    ep = ''
    for x in g:
        if x > len(arr)/2:
            gam += '1'
            ep += '0'
        else:
            gam += '0'
            ep += '1'
    print(int(gam, 2)*int(ep, 2))

if __name__ == "__main__":
    main()

