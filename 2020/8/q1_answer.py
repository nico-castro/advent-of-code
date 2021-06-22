#!/usr/local/bin/python3

def parse_line(line: str) -> (str, int):
    cmd = line.split(" ")[0]
    val = int(line.split(" ")[1])
    return cmd, val 

def main():
    commands = []
    ACC = 0
    with open('input.txt', 'r') as f:
        for line in f:
            commands.append(line.rstrip())

    i = 0
    while i <= len(commands):
        cmd, val = parse_line(commands[i])        
        commands[i] = 'end 0'
        if cmd == 'acc':
            ACC = ACC + val
            i = i + 1
        elif cmd == 'nop':
            i = i + 1 
        elif cmd == 'jmp':
            i = i + val
        elif cmd == 'end':
            break

    print(ACC)

if __name__ == "__main__":
    main()

