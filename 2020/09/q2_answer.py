#!/usr/local/bin/python3
def parse(name: str) -> []:
    XMAS = []
    with open(name, 'r') as f:
        for line in f:
            XMAS.append(int(line.rstrip()))
    return XMAS

def main():
    xmas = parse('input.txt')
    target = 1721308972

    start = end = 0
    for i in range(len(xmas)): 
        j = i + 1 
        total = xmas[i] + xmas[j]
        while total <= target:
            if total == target:
                start, end = i, j
                break
            else:
                j = j + 1
                total = total + xmas[j]
        if start and end:
            break

    mn = mx = xmas[start]
    for i in range(start, end+1):
        if xmas[i] > mx:
            mx = xmas[i]
        if xmas[i] < mn:
            mn = xmas[i]
    print(f"{mn} + {mx} = {mn+mx}" )

if __name__ == "__main__":
    main()

