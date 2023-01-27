import sys
lines = list(map(str.strip, sys.stdin.readlines()))



i = 1
while i < len(lines):
    n = int(lines[i])
    result = []
    i+=1
    seqs = []
    for _ in range(n):
        nums = list(map(int, lines[i].split()))
        seqs.append(nums)
        i+=1
    want = set([i for i in range(1, n+1)])
    counts = {}
    for j in range(len(seqs[0])):
        for k in range(len(seqs)):
            counts[seqs[k][j]] = counts.get(seqs[k][j], 0) + 1
        biggest = [-1,-1]
        for key, val in counts.items():
            if val > biggest[1]:
                biggest = [key, val]
        result.append(biggest[0])
        del counts[biggest[0]]
        want.remove(biggest[0])
    print(*result, want.pop())



        