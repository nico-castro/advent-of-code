#!/usr/local/bin/python3

def main():
    arr = []
    with open('input.txt') as f:
        for line in f:
            arr.append(line.rstrip())

    def O2_filter(arr, i):
        ones = 0
        zeroes = 0
        for a in arr:
            if a[i] == '1':
                ones += 1
            else:
                zeroes += 1
        if ones >= zeroes:
            return list(filter(lambda x: x[i] == '1', arr))
        else:
            return list(filter(lambda x: x[i] == '0', arr))

    def CO2_filter(arr, i): 
        ones = 0
        zeroes = 0
        for a in arr:
            if a[i] == '0':
                zeroes += 1
            else:
                ones += 1
        if zeroes <= ones:
            return list(filter(lambda x: x[i] == '0', arr))
        else:
            return list(filter(lambda x: x[i] == '1', arr))
    O2 = arr.copy()
    CO2 = arr.copy()        
    for i in range(len(O2[0])):
        if len(O2) == 1:
            break
        O2 = O2_filter(O2, i)
    for i in range(len(CO2[0])):
        if len(CO2) == 1:
            break
        CO2 = CO2_filter(CO2, i)
    print(int(O2[0],2)*int(CO2[0], 2))
    
if __name__ == "__main__":
    main()

