import sys
lines = list(map(str.strip, sys.stdin.readlines()))

n, m = map(int, lines[0].split(" "))
adj_lists={i:0 for i in range(1, n+1)}
most_powerful = [n]
i = 1
def add_relation(fr, to):
    if to > fr:
        if adj_lists[fr] == 0:
            most_powerful[0] -=1
        adj_lists[fr] += 1

def remove_relation(fr, to):
    if to > fr:
        adj_lists[fr] -= 1
        if adj_lists[fr] == 0:
            most_powerful[0] += 1

while m > 0:
    fr, to = map(int, lines[i].split(" "))
    add_relation(fr, to)
    add_relation(to, fr)
    i+=1
    m-= 1
q = int(lines[i])
i+=1
queries = []
while q > 0:
    queries.append(list(map(int, lines[i].split(" "))))
    q-=1
    i+=1
for q in queries:
    if len(q) == 1: 
        print(most_powerful[0])
        continue
    if q[0] == 1:
        add_relation(q[1], q[2])
        add_relation(q[2], q[1])
    else:
        remove_relation(q[1], q[2])
        remove_relation(q[2], q[1])

