import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def sum_of_all(xs):
    total = sum(xs)
    result = []
    for i in range(len(xs)):
        result.append(total)
        total -= xs[i]
    return result

for i in range(1, len(lines), 3):
    a = list(map(int, lines[i+1].split(" ")))
    b = list(map(int, lines[i+2].split(" ")))
    unis = {}
    for j in range(len(a)):
        if a[j] not in unis: unis[a[j]] = []
        unis[a[j]].append(b[j])
    for key in unis:
        unis[key].sort(key=lambda x: -x)
        unis[key] = sum_of_all(unis[key])
    
    total = sum([unis[key][0] for key in unis])
    for k in range(1, len(a) + 1):
        curr = total
        to_delete = []
        for uni in unis:
            if k > len(unis[uni]):
                to_delete.append(uni)
                curr -= unis[uni][0]
                continue
            cantgo = len(unis[uni]) % k
            if cantgo != 0:
                curr -= unis[uni][-cantgo]
        for uni in to_delete:
            total -= unis[uni][0]
            del unis[uni]
        print(curr, end= " ")
    print()