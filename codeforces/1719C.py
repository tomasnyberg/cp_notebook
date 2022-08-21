import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
while i < len(lines):
    n, q = map(int, lines[i].split(" "))
    i+=1
    nums = list(map(int, lines[i].split(" ")))
    i+=1
    queries = []
    while q > 0:
        queries.append(list(map(int, lines[i].split(" "))))
        q-=1
        i+=1
    # If there is a fighter to the left of the current figher with strength greater than it, they will never
    # Win a single fight.
    # How good the current best guy is, and where he is
    biggest = None
    #dp[i] = How many the guy at i will win before losing
    dp = []
    for idx, fighter in enumerate(nums):
        if not biggest or fighter > biggest[0]:
            if biggest:
                dp[biggest[1]] = idx - biggest[1] - 1
                if biggest[1] != 0:
                    dp[biggest[1]] += 1
            biggest = [fighter, idx]
            dp.append(10**9)
        else:
            dp.append(0)
    for fighter, rounds in queries:
        fighter -=1
        # How many rounds before he gets to fight
        if fighter != 1 and fighter != 0:
            rounds -= fighter - 1
        if rounds < 0:
            print(0)
        else:
            print(min(rounds, dp[fighter]))
    
        