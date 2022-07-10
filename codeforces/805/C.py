import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def solve(stops, start, end):
    if start not in stops or end not in stops:
        print("NO")
        return
    if stops[start][0] <= stops[end][-1]:
        print("YES")
    else:
        print("NO")

i = 2
while i < len(lines):
    n, queries = map(int, lines[i].split(" "))
    i+=1
    nums = list(map(int, lines[i].split(" ")))
    stops = {}
    for idx, x in enumerate(nums):
        if x not in stops: stops[x] = []
        stops[x].append(idx)
    # print(nums)
    # print(stops)
    # print()
    i+=1
    while queries > 0:
        start, end = map(int, lines[i].split(" "))
        solve(stops, start, end)
        i +=1
        queries -= 1
    i+=1