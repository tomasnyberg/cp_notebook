import sys
lines = list(map(str.strip, sys.stdin.readlines()))


def solve(adj_lists, num_set, start):
    curr = start
    def dfs(curr, curr_taken, paths_taken):
        for nbr in adj_lists[curr]:
            path = str(curr) + " " + str(nbr)
            path2 = str(nbr) + " " + str(curr)
            if path not in paths_taken:
                removed = dfs(nbr, set([*curr_taken, nbr]), set([*paths_taken, path, path2]))
                if len(num_set.difference(removed)) == 0:
                    return num_set
        return curr_taken
    to_remove = dfs(curr, set([start]), set())
    if len(num_set.difference(to_remove)) == 0:
        print("YES")
    else:
        print("NO")

i = 0
n = int(lines[0])
adj_lists = {a: [] for a in range(1, n+1)}
i+=1 
while n > 1:
    fr, to = map(int, lines[i].split(" "))
    adj_lists[fr].append(to)
    adj_lists[to].append(fr)
    i +=1
    n-=1
queries = int(lines[i])
i+=1
while queries > 0:
    nums = list(map(int, lines[i+1].split(" ")))
    start = nums[0]
    num_set = set(nums)
    solve(adj_lists, num_set, start)
    i+=2
    queries -=1
