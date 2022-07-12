import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def solve(sequence, init):
    for c in sequence:
        if c == 'D':
            init += 1
            if init == 10:
                init = 0
        else:
            init -= 1
            if init == -1:
                init = 9
    print(init, end=" ")


i = 1
while i < len(lines):
    n = int(lines[i])
    i+=1
    nums = list(map(int, lines[i].split(" ")))
    sequences = []
    i+=1
    while n > 0:
        sequences.append(lines[i].split(" ")[1])
        n -=1
        i+=1
    for j in range(len(nums)):
        solve(sequences[j], nums[j])
    print()
