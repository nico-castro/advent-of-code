#import ipdb

a = []
with open('D2_input.txt', 'r') as file:
    for line in file:
        a.append(line.rstrip('\n'))

valid = 0

for line in a:
    _min = (int)(line.split('-')[0])
    _max = (int)(line.split('-')[1].split(' ')[0])
    _char = line.split(' ')[1][0]
    password = line.split(':')[1][1:]

#    ipdb.set_trace()

    def appearances(_char, password):
        occurs = 0
        for x in password:
            if x == _char:
              occurs += 1
        return occurs

    occurances = appearances(_char, password)

    if occurances <= _max and occurances >= _min:
        valid += 1

print(valid)
