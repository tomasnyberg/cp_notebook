import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 3):
    a, b, k = map(int, lines[i].split(" "))
    boys = list(map(int, lines[i+1].split(" ")))
    girls = list(map(int, lines[i+2].split(" ")))
    boy_pairs = {}
    for j in range(len(boys)):
        if boys[j] not in boy_pairs: boy_pairs[boys[j]] = set()
        boy_pairs[boys[j]].add(girls[j])
    girl_counts = {girl: 0 for girl in girls}
    for girl in girls:
        girl_counts[girl] += 1
    result = 0
    for boy, partners in boy_pairs.items():
        total_added = 0
        for partner in partners:
            total_added += k - (len(partners) - 1) - girl_counts[partner]
            result += k - (len(partners) - 1) - girl_counts[partner]
        # print("boy", boy, "contributed with", total_added)
    print(result//2)