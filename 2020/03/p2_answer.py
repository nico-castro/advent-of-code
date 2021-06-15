import ipdb

inpt = []
with open('input.txt', 'r') as file:
    for line in file:
        inpt.append(line.rstrip('\n'))

def traverse(rise, run):
    x, y = 0,0
    trees = 0
    length = len(inpt[0])
#    ipdb.set_trace()
    while y < len(inpt):
        if (inpt[y][x] == '#'):
            trees += 1
        x = (x + run) % length
        y += rise
    return trees

result = 1
slopes = [(1,1), (1, 3), (1, 5), (1, 7), (2, 1)]

for rise, run in slopes:
    result = result * traverse(rise, run)

print(result)
