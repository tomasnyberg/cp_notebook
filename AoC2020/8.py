import sys
lines = list(map(str.strip, sys.stdin.readlines()))

commands = []
for line in lines:
    commands.append(line)

for i in range(len(commands)):
    command, num = commands[i].split(" ")
    num = int(num)
    commands[i] = [command, num]

def solve():
    visited = set()
    i = 0
    accumulator = 0
    while True:
        if i == len(commands):
            return [True, accumulator]
        if i in visited:
            return [False, accumulator]
        visited.add(i)
        if commands[i][0] == 'nop':
            i+=1
        elif commands[i][0] == 'acc':
            accumulator += commands[i][1]
            i+=1
        else:
            i+= commands[i][1] 

def part_two():
    other = {'nop':'jmp', 'jmp':'nop'}
    for i in range(len(commands)):
        cmd, num = commands[i]
        if cmd in other:
            commands[i][0] = other[cmd]
            res = solve()
            if res[0]:
                return res
            commands[i][0] = cmd
print("Part one:", solve()[1])
print("Part two:", part_two()[1])

