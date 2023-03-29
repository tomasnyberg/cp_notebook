import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
while i < len(lines):
    n, m = map(int, lines[i].split())
    cards = []
    for _ in range(n):
        cards.append(list(map(int, lines[i+1].split())))
        i += 1
    i += 1
    transposed = [[0 for _ in range(n)] for _ in range(m)]
    # Transpose the cards matrix
    for j in range(n):
        for k in range(m):
            transposed[k][j] = cards[j][k]
    result = 0
    for xs in transposed:
        xs.sort()
        # print(xs)
        running = 0
        for j in range(len(xs)):
            contribute = ((xs[j] - (running / (j))) * j) if j > 0 else 0
            result += contribute 
            # print(xs[j], "contributes with", contribute, "to result")
            running += xs[j]
    print(int(result))



    
