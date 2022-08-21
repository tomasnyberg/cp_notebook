import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def nPr(n, r):
    import math
    return math.factorial(n) // math.factorial(n-r)

def nCr(n,r):
    import math
    return math.factorial(n) // (math.factorial(r)*(math.factorial(n-r)))

n, k = map(int, lines[0].split(" "))
change = {} # point in time -> [turned on, turned off]
lines = list(map(lambda x: list(map(int, x.split(" "))), lines[1:]))
for turnon, turnoff in lines:
    if turnon not in change: change[turnon] = [0,0]
    if turnoff not in change: change[turnoff] = [0,0]
    change[turnon][0]+=1
    change[turnoff][1]+=1
changes = [(time,change[time][0], change[time][1]) for time in change]
changes.sort(key=lambda x: x[0])
result = 0
on = 0
diff = 0
for time, up, down in changes:
    on += up
    print("at time", time, "on:" , on, "diff:", diff)
    if on >= k:
        to_add = nCr(on, k)
        result += to_add
    on -= down
print(changes)
print(result)



