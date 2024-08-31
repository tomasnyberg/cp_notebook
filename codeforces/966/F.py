import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('codeforces/966/in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict



ii = 1
while ii < len(lines):
    n, k = map(int, lines[ii].split())
    ii+=1
    rects = []
    for _ in range(n):
        rects.append(list(map(int, lines[ii].split())))
        ii+=1
    dp = [[10**25]*(k+1) for _ in range(n+1)]
    for i in range(len(dp)):
        dp[i][0] = 0
    for i in range(1, len(dp)):
        rows, cols = rects[i-1]
        curr_points = 0
        ops = 0
        amounts = {}
        while rows and cols:
            if rows == 1 and cols == 1:
                ops+=1
                curr_points += 2
                amounts[curr_points] = ops
                break
            if rows <= cols:
                ops += rows
                cols -= 1
            else:
                ops += cols
                rows -= 1
            curr_points += 1
            amounts[curr_points] = ops
        # print(rows, cols, amounts)
        # print()
        amounts = list(sorted(amounts.items()))
        for j in range(1, len(dp[0])):
            dp[i][j] = dp[i-1][j] # Just take previous result
            for score, ops in amounts:
                if j - score < 0:
                    break
                dp[i][j] = min(dp[i][j], dp[i-1][j-score] + ops)
    # for xs in dp:
    #     print(xs)
    print(dp[-1][-1] if dp[-1][-1] != 10**25 else -1)