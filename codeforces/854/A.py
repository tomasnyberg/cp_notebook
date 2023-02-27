import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, m = map(int, lines[i].split())
    m_nums = list(map(int, lines[i + 1].split()))
    new_m_nums = []
    seen = set()
    for x in m_nums:
        if x not in seen:
            new_m_nums.append(x)
            seen.add(x)
    m = len(new_m_nums)
    nums = [i for i in range(1, n+1)]
    seen_indices = {}
    for i in range(1, n+1):
        seen_indices[i] = [-i + 1]
    for idx, x in enumerate(m_nums):
        if x not in seen_indices: continue
        seen_indices[x].append(idx)
    for key in seen_indices:
        seen_indices[key].append(m)
    ans = []
    for key in seen_indices:
        for j in range(1, len(seen_indices[key])):
            if seen_indices[key][j] - seen_indices[key][j-1] >= n:
                nums[seen_indices[key][j-1]] = key
    for i in range(1, n+1):
        for j in range(1, len(seen_indices[i])):
            if seen_indices[i][j] - seen_indices[i][j-1] >= n:
                ans.append(seen_indices[i][j-1] + n)
                break
        else:
            ans.append(-1)
    print(seen_indices)
    print(*ans)