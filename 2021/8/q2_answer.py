#!/usr/local/bin/python3

#  aaa
# b   c
# b   c
#  ddd
# e   f
# e   f
#  ggg


def missing_char(s):
    d = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1}
    for c in s:
        d[c] -= 1
    for c in d:
        if d[c] == 1:
            return c


def parse_inputs(inputs):
    ret = {}
    b = {}
    for i in inputs:
        if len(i) == 7:
            b[8] = i
        elif len(i) == 3:
            b[7] = i
        elif len(i) == 4:
            b[4] = i
        elif len(i) == 2:
            b[1] = i

    b[6] = [x for x in inputs if len(x) == 6 and missing_char(x) in b[1]][0]
    c = missing_char(b[6])
    f = [x for x in b[1] if x != c][0]
    b[0] = [x for x in inputs if len(x) == 6 and missing_char(x) in b[4] and missing_char(x) in b[6]][0]
    b[9] = [x for x in inputs if len(x) == 6 and sorted(x) != sorted(b[6]) and sorted(x) != sorted(b[0])][0]
    b[5] = ''.join(b[9].split(c))
    b[2] = [x for x in inputs if len(x) == 5 and f not in x][0]
    b[3] = [x for x in inputs if len(x) == 5 and sorted(x) != sorted(b[5]) and sorted(x) != sorted(b[2])][0]

    for k, v in b.items():
        s = ''.join(sorted(v))
        ret[s] = k
    return ret


def sum_outputs(key: {str: int}, outputs: [str]) -> int:
    v = ''
    for o in outputs:
        s = ''.join(sorted(o))
        v += str(key[s])
    return int(v)


def main():
    arr = []
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip().split(' | ')
            arr.append((line[0].split(' '), line[1].split(' ')))

    tot = 0
    for ins, outs in arr:
        key = parse_inputs(ins)
        tot += sum_outputs(key, outs)
    print(tot)


if __name__ == "__main__":
    main()
