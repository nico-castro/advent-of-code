a = []
with open('D1_input.txt', 'r') as file:
    for line in file:
        a.append((int)(line.rstrip('\n')))

for x in range(len(a)):
    for y in range(x+1, len(a)):
        for z in range(y+1, len(a)): 
            if a[x] + a[y] + a[z]== 2020:
                print(a[x]*a[y]*a[z])
    
