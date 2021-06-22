#!/usr/local/bin/python3

def parse_line(line: str) -> (str, int):
    cmd = line.split(" ")[0]
    val = int(line.split(" ")[1])
    return cmd, val 

def detect_loop(cmds: []) -> bool:
    i = 0
    while i < len(cmds):
        cmd, val = parse_line(cmds[i])
        cmds[i] = 'end 0'
        if cmd == 'acc':
            i = i + 1
        elif cmd == 'nop':
            i = i + 1
        elif cmd == 'jmp':
            i = i + val
        elif cmd == 'end':
            return True
    return False
 

def main():
    commands = []
    with open('input.txt', 'r') as f:
        for line in f:
            commands.append(line.rstrip())

    for i in range(len(commands)):
        cmd, val = parse_line(commands[i])
        if cmd == 'acc':
            continue
        elif cmd == 'nop':
            test_cmds = commands[:]
            test_cmds[i] = " ".join(('jmp', str(val)))
            if detect_loop(test_cmds):
                i = i + 1
            else:
                commands[i] = " ".join(('nop', str(val)))
                break
        elif cmd == 'jmp':
            test_cmds = commands[:]
            test_cmds[i] = " ".join(('nop', str(val)))
            if detect_loop(test_cmds):
                i = i + 1
            else:
                commands[i] = " ".join(('nop', str(val)))
                break

    ACC = 0
    i = 0
    while i < len(commands):
        cmd, val = parse_line(commands[i])
        if cmd == 'acc':
            ACC = ACC + val
            i = i + 1
        elif cmd == 'nop':
            i = i + 1
        elif cmd == 'jmp':
            i = i + val
    print(ACC)

if __name__ == "__main__":
    main()

