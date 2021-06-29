#!/usr/local/bin/python3
def parse(name: str) -> []:
    XMAS = []
    with open(name, 'r') as f:
        for line in f:
            XMAS.append(int(line.rstrip()))
    return XMAS

def main():
    xmas = parse('input.txt')
    window = 25

    for i in range(window, len(xmas)): 
        preamble = xmas[i-window:i]
        target = xmas[i]
        good = False
        for j in range(len(preamble)):
            for k in range(j, len(preamble)):
                if preamble[j] + preamble[k] == target:
                    good = True
        if not good:
            print(target)

if __name__ == "__main__":
    main()

