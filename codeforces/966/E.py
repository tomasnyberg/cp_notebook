import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('codeforces/966/in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

def cumsum2d(arr):
    result = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr[0])):
            sum += arr[i][j]
            result[i][j] = sum + (result[i-1][j] if i > 0 else 0)
    return result

# How you actually query the 2d prefix array
def query(cs2d, a, b, A, B): # a, b are the coordinates of the top left corner, A, B are the coordinates of the bottom right corner
    result = 0
    result += cs2d[A][B]
    result += cs2d[a-1][b-1] if a-1 >= 0 and b-1 >= 0 else 0
    result -= cs2d[a-1][B] if a-1 >= 0 else 0
    result -= cs2d[A][b-1] if b-1 >= 0 else 0
    return result

def calculate_score(matrix, k):
    k-=1
    cs2d = cumsum2d(matrix)
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i + k >= len(matrix) or j + k >= len(matrix[0]):
                break
            query_result = query(cs2d, i, j, i + k, j + k)
            result += query_result
    return result

for ii in range(1, len(lines), 3):
    n, m, k = map(int, lines[ii].split())
    w = int(lines[ii+1])
    gorillas = list(map(int, lines[ii+2].split()))
    gorillas.sort()
    # 1. How many times does the sliding box go over each particular cell?
    # The middle is the most important, no?
    # How do we place the biggest gorillas in the middle?
    # Perhaps more importantly, how do we answer 1?
    # - by doing 2d range sum queries, ez
    # spiral pattern? NO
    # Place the gorillas as centrally as possible 
    # How??? 
    matrix = [[0]*m for _ in range(n)]
    # 1: how many do you lose at the start? Depends how much below you the square starts.
    # so max(0, k - (row + 1))?
    # and same for col: max(0, k - (col + 1))
    # and how many do you lose at the end: 
    # 2: How many do you lose at the end? 
    # rows: max(0, (n - row))
    # It can at most start at n-k
    # so we will lose row - (n-k)
    # cols:
    # we will lose col - (m - k)
    counts = []
    for row in range(n):
        for col in range(m):
            lose_start_row = max(0, (k - (row + 1)))
            lost_start_col = max(0, (k - (col + 1)))
            lose_end_row = max(0, row - (n - k))
            lose_end_col = max(0, col - (m - k))
            remaining = (k - lose_start_row - lose_end_row)*(k - lost_start_col - lose_end_col)
            counts.append(remaining)
    counts.sort()
    result = 0
    for g in gorillas[::-1]:
        result += counts.pop() * g
    print(result)

    gorillas = [
        [1,1,1,0],
        [1,1,1,1],
        [0,1,1,0]
    ]
    # X X X X