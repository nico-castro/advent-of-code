#import ipdb

a = []
with open('D2_input.txt', 'r') as file:
    for line in file:
        a.append(line.rstrip('\n'))

valid = 0

for line in a:
    pos1 = (int)(line.split('-')[0])
    pos2 = (int)(line.split('-')[1].split(' ')[0])
    _char = line.split(' ')[1][0]
    password = line.split(':')[1][1:]

#    ipdb.set_trace()

    if  (password[pos1 - 1] == _char or password[pos2 - 1] == _char) and not (password[pos1 - 1] == _char and password[pos2 - 1] == _char):
        valid += 1

print(valid)
