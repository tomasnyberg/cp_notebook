import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def input_range(s, ranges):
    split= s.split("-")
    ranges.append([int(split[0]), int(split[1])])


ranges = []
i = 0
while lines[i] != "":
    curr= lines[i]
    split = curr.split(" ")
    print(split[-1], split[-3])
    a, b= (split[-1], split[-3])
    input_range(a, ranges)
    input_range(b, ranges)
    i+=1
i+=1
while lines[i] != "":
    i+=1

tickets = []
i+=2
while i < len(lines):
    tickets.append(list(map(int, lines[i].split(","))))
    i+=1

def check_ticket(ticket, ranges):
    for j in range(len(ticket)):
        curr = ticket[j]
        good = False
        for start, end in ranges:
            if start <= curr <= end:
                good = True
                break
        if not good:
            ticket[j] = -ticket[j]

result = 0
new_tickets = []
for ticket in tickets:
    check_ticket(ticket, ranges)
    if all(x >= 0 for x in ticket):
        new_tickets.append(ticket)
print(new_tickets)
    


