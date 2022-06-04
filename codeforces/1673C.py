import sys
 
lines = list(map(str.strip, sys.stdin.readlines()))
mod = 1000000007
N = 40004
M = 502
all_pals = [0]
for i in range(1, 2*N):
    if str(i) == str(i)[::-1]:
        all_pals.append(i)
        
 
dp = [[0 for _ in range(M)] for x in range(N)]
for i in range(1, M):
    dp[0][i] = 1
for i in range(1, N):
    dp[i][0] = 0
 
for i in range(1, N):
    for j in range(1, M):
        if(all_pals[j] <= i):
            dp[i][j]=(dp[i][j-1]+dp[i-all_pals[j]][j])%mod
        else:
            dp[i][j] = dp[i][j-1]
 
for line in lines[1:]:
    n = int(line)
    print(dp[n][M-1])