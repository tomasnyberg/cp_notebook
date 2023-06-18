import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    robot_lines = []
    robot_lines.sort()
    bad = False
    for x in nums:
        if x == 0:
            robot_lines.append([0])
            continue
        for xs in robot_lines:
            if xs[-1] == x - 1:
                xs.append(x)
                break
        else:
            bad = True
            break
    if bad:
        print("NO")
    else:
        print("YES")
            