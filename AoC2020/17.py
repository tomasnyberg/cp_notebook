import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

matrix = []

def solve(part2):
    dirs = []
    if part2:
        dirs = [(x,y,z,w) for x in [-1,0,1] for y in [-1,0,1] for z in [-1,0,1] for w in [-1,0,1] if x or y or z or w]
    else:
        dirs = [(x,y,z) for x in [-1,0,1] for y in [-1,0,1] for z in [-1,0,1] if x or y or z]
    size = 30
    grid = []
    if part2:
        grid = [[[[0 for w in range(size)] for k in range(size)] for j in range(size)] for i in range(size)]
    else:
        grid = [[[0 for k in range(size)] for j in range(size)] for i in range(size)]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                # four dimensions
                if part2:
                    grid[size//2][size//2+i][size//2+j][size//2] = 1
                else:
                    grid[size//2][size//2+i][size//2+j] = 1

    def check_neighbours(i,j,k,z=0):
        result = 0
        for d in dirs:
            if part2:
                if 0 <= i+d[0] < size and 0 <= j+d[1] < size and 0 <= k+d[2] < size and 0 <= z+d[3] < size:
                    if grid[i+d[0]][j+d[1]][k+d[2]][z+d[3]] == 1:
                        result += 1
            else:
                if 0 <= i+d[0] < size and 0 <= j+d[1] < size and 0 <= k+d[2] < size:
                    if grid[i+d[0]][j+d[1]][k+d[2]] == 1:
                        result += 1
        return result

    def check_all(grid):
        # Create a copy of grid in 4d
        new_grid = []
        if part2:
            new_grid = [[[[grid[i][j][k][z] for z in range(size)] for k in range(size)] for j in range(size)] for i in range(size)]
        else:
            new_grid = [[[grid[i][j][k] for k in range(size)] for j in range(size)] for i in range(size)]
        # loop through the whole grid
        for i in range(0,size):
            for j in range(0,size):
                for k in range(size):
                    if part2:
                        for z in range(size):
                            neighbours = check_neighbours(i,j,k,z)
                            if grid[i][j][k][z] == 0 and neighbours == 3:
                                new_grid[i][j][k][z] = 1
                            if grid[i][j][k][z] == 1 and (neighbours < 2 or neighbours > 3):
                                new_grid[i][j][k][z] = 0
                    else:
                        neighbours = check_neighbours(i,j,k)
                        if grid[i][j][k] == 0 and neighbours == 3:
                            new_grid[i][j][k] = 1
                        if grid[i][j][k] == 1 and (neighbours < 2 or neighbours > 3):
                            new_grid[i][j][k] = 0
        return new_grid

    for i in range(6):
        grid = (check_all(grid))
    if part2:
        return sum([sum([sum([sum(grid[i][j][k]) for k in range(size)]) for j in range(size)]) for i in range(size)])
    else:
        return sum([sum([sum(grid[i][j]) for j in range(size)]) for i in range(size)])

print("Part one:", solve(False))
print("Part two:", solve(True))