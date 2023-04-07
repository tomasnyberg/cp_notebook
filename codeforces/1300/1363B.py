import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for s in lines[1:]:
    counts = {'0':0, '1':0}
    for c in s:
        counts[c] +=1
    result = len(s)
    seensofar = {'0':0, '1':0}
    for idx, x in enumerate(s):
        seensofar[x]+=1
        counts[x]-=1
        # Cost to change all into either 0 or 1, and the rest to either as well
        for c1 in ['0', '1']:
            for c2 in ['0', '1']:
                result = min(result, seensofar[c1] + counts[c2])
    print(result)



