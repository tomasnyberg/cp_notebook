import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def print_grid(grid):
    for xs in grid:
        print(xs)

def solve(grid):
    result = 0
    for steps in range(0, len(grid) // 2):
        for i in range(steps, len(grid) - steps - 1):
            # Fairly confident about a and b
            a = grid[steps][i]
            b = grid[i][len(grid) - steps - 1]
            
            c = grid[len(grid) - steps - 1][len(grid) - 1 -i] # Wrong
            d = grid[len(grid) - 1 -i][steps]
            # print(a,b,c,d)
            # print(len(grid) - steps - 1, len(grid) - steps - i - 1)
            # print(len(grid) - steps - i - 1, steps)
            if a == b == c == d:
                continue
            sum = a + b + c + d
            result += min(4 - sum, abs(0 - sum))
        # print("result after ", steps, "steps", result)
    print(result)

    
# a = [steps, i]
# b = [i, 5 - steps - 1]
# c = [5 - 0 - 1 - steps, 5 - 0 - i - 1]
# d = [5 - 0 - i - 1, steps]


i = 1
while i < len(lines):
    n = int(lines[i])
    grid = []
    i+=1
    while n > 0:
        grid.append(list(map(int, lines[i])))
        n-=1
        i+=1
    solve(grid)