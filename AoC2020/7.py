import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def dfs(curr):
    if curr == "shinygold": return True
    for nbr in adj_lists[curr]:
        if dfs(nbr):
            return True

adj_lists = {}
for line in lines:
    split = line.split(" ")
    osplit = line.split(" contain ")[1].split(", ")
    fr = split[0] + split[1]
    adj_lists[fr] = {}
    for other in osplit:
        split = other.split(" ")
        count = split[0]
        if count == "no": continue
        to = split[1] + split[2]
        adj_lists[fr][to] = count

result = 0
for key in adj_lists:
    if key == "shinygold": continue
    if dfs(key): result +=1
print(result)