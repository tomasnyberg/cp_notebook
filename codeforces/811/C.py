import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    num = int(line)
    if num < 10:
        print(num)
        continue
    def dfs(remaining, taken):
        if remaining == 0:
            for x in taken:
                print(x, end="")
            print()
            return True
        for i in range(9, 0, -1):
            if i in taken or remaining - i < 0: continue
            if dfs(remaining - i, [i, *taken]):
                return True
            
    dfs(num, [])