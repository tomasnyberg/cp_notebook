import sys, random
lines = list(map(str.strip, sys.stdin.readlines()))

# with open("in", "w") as f:
#     for i in range(10):
#         for i in range(25):
#             for j in range(25):
#                 f.write(str(random.randint(-100, 100)) + " ")
#             f.write("\n")
#         f.write("\n")

def solve(matrix):
    pass

i = 0
while i < len(lines):
    matrix = []
    for _ in range(25):
        matrix.append(list(map(int, lines[i].split(" "))))
        i+=1
    i+=1
    total = 0
    for xs in matrix:
        total += sum(xs)
    print("total is", total)
    