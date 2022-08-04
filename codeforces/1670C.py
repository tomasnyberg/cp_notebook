import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(2, len(lines), 4):
    a = list(map(int, lines[i].split(" ")))
    b = list(map(int, lines[i+1].split(" ")))
    c = list(map(int, lines[i+2].split(" ")))
    taken = set()
    looking_for = set() # Pairs that we are looking for
    result = 1
    for j in range(len(a)):
        if c[j] != 0:
            taken.add(c[j])
            continue
        pair = str(a[j]) + " " + str(b[j])
        if pair in looking_for:
            taken.update([a[j], b[j]])
            result *= 2
            continue
        looking_for.add(str(b[j]) + " " + str(a[j]))
        if a[j] == b[j]:
            taken.add(a[j])
    must_take_if_seen = set()
    # print(a)
    # print(b)
    # print(c)
    for j in range(len(a)):
        # print(taken)
        # print(must_take_if_seen)
        if c[j] == 0 and a[j] not in must_take_if_seen and b[j] not in must_take_if_seen:
            if a[j] in taken:
                taken.add(b[j])
                continue
            if b[j] in taken:
                taken.add(a[j])
                continue
            result *=2
            must_take_if_seen.update([a[j], b[j]])
        elif c[j] == 0 and a[j] in must_take_if_seen and a[j] not in taken:
            taken.add(a[j])
            must_take_if_seen.add(b[j])
        elif c[j] == 0 and b[j] in must_take_if_seen and b[j] not in taken:
            taken.add(b[j])
            must_take_if_seen.add(b[j])
        elif c[j] != 0:
            if a[j] != c[j] and a[j] not in taken:
                must_take_if_seen.add(a[j])
            if b[j] != c[j] and a[j] not in taken:
                must_take_if_seen.add(b[j])
            if a[j] == c[j]: taken.add(a[j])
            if b[j] == c[j]: taken.add(b[j])
        else:
            "case you missed"
    print(result)
    # print()


