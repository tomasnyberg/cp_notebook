import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def part_one():
    result = 0
    curr = set()
    for line in lines:
        if line == "":
            result += len(curr)
            curr = set()
        else:
            curr |= set(line)
    return result + len(curr)

def part_two():
    result = 0
    curr = []
    for line in lines:
        if line == "":
            s = curr[0]
            for os in curr:
                s &= os
            result += len(s)
            curr = []
        else:
            curr.append(set(line))
    return (result)

print("Part one:", part_one())
print("Part two:", part_two())