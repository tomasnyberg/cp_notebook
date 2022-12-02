import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def input_range(s, ranges, field, range_dict):
    split= s.split("-")
    ranges.append([int(split[0]), int(split[1]), field])
    if field not in range_dict:
        range_dict[field] = []
    range_dict[field].append([int(split[0]), int(split[1])])

rd = {}

ranges = []
i = 0
while lines[i] != "":
    curr= lines[i]
    split = curr.split(" ")
    field = curr.split(":")[0]
    a, b= (split[-1], split[-3])
    input_range(a, ranges, field, rd)
    input_range(b, ranges, field, rd)
    i+=1
i+=1
while lines[i] != "":
    i+=1

my_ticket = list(map(int, lines[i-1].split(",")))
print(my_ticket)
tickets = []
i+=2
while i < len(lines):
    tickets.append(list(map(int, lines[i].split(","))))
    i+=1


possible = []
for j in range(len(tickets[0])):
    possible.append(set())

def check_ticket(ticket, ranges):
    for j in range(len(ticket)):
        curr = ticket[j]
        good = False
        for start, end, field in ranges:
            if start <= curr <= end:
                good = True
                possible[j].add(curr)
        if not good:
            ticket[j] = -ticket[j]

result = 0
new_tickets = []
for ticket in tickets:
    check_ticket(ticket, ranges)
    if all(x >= 0 for x in ticket):
        new_tickets.append(ticket)

print(rd)
result = []
for j in range(len(possible)):
    result.append(set())
for j in range(len(possible)):
    s = possible[j]
    for field, rngs in rd.items():
        good = True
        for x in s:
            if not any(start <= x <= end for start, end in rngs):
                good = False
                break
        if good:
            result[j].add(field)
taken = set()
while True:
    if all(len(s) == 1 for s in result):
        break
    for j in range(len(result)):
        if len(result[j]) == 1:
            taken |= result[j]
            continue
        for x in taken:
            if x in result[j]:
                result[j].remove(x)

mul = 1
for j in range(len(result)):
    if result[j].pop().split(" ")[0] == "departure":
        mul *= my_ticket[j]
print(mul)
        
        




