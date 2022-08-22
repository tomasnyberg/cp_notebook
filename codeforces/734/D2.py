import sys
lines = list(map(str.strip, sys.stdin.readlines()))

# Going to assume we have a possible solution if we get here
def print_solution(n, m, horizontal, vertical):
    squarepos = [[0, 1], [1,1], [1, 0]]
    result = [['.' for i in range(m)] for _ in range(n)]
    currchar = 0
    if n % 2 == 1: # we need to fill the bottom row with horizontal blocks
        for i in range(0,m, 2):
            result[-1][i] = chr(currchar+97)
            result[-1][i+1] =chr(currchar+97) 
            currchar += 1 
            currchar %= 26
        horizontal -= m//2
    if m % 2 == 1: # we need to fill the rightmost col with vertical blocks
        for i in range(0,n, 2):
            result[i][-1] = chr(currchar+97)
            result[i+1][-1] =chr(currchar+97)
            currchar += 1
            currchar %= 26
        vertical -= n//2
    for i in range(0, n if n % 2 == 0 else n-1, 2): # Skip the last row in the case that n is uneven
        for j in range(0, m if m % 2 == 0 else m-1, 2): # Same here
            if horizontal > 0:
                horizontal -= 2
                for k in range(2):
                    result[i+k][j] = chr(currchar+97)
                    result[i+k][j+1] = chr(currchar+97)
                    currchar += 1
                    currchar %= 26
            else:
                for k in range(2):
                    result[i][j+k] = chr(currchar + 97)
                    result[i+1][j+k] = chr(currchar + 97)
                    currchar += 1
                    currchar %= 26
    for xs in result:
        [print(x, end="") for x in xs]
        print()


for line in lines[1:]:
    n, m, k = list(map(int, line.split(" ")))
    # print(n, m, "horizontal:", k, "vertical:", (n*m)//2 -k)
    horizontal = k
    vertical = (n*m)//2 - k
    if n % 2 == 1: # We need to make 
        needed_for_col = m//2
        if k >= m//2 and (k - needed_for_col)%2 == 0:
            print("YES")
            print_solution(n, m, horizontal, vertical)
        else:
            print("NO")
        # print("YES" if k >= m//2 and (k - needed_for_col)%2 == 0 else "NO")
    elif m % 2 == 1:
        needed_for_row = n // 2
        amount = (n*m)//2 -k
        # print("YES" if amount >= n // 2 and (amount - needed_for_row)%2==0 else "NO")
        if amount >= n // 2 and (amount - needed_for_row)%2==0:
            print("YES")
            print_solution(n, m, horizontal, vertical)
        else:
            print("NO")
    else:
        if k % 2 == 0:
            print("YES")
            print_solution(n, m, horizontal, vertical)
        else:
            print("NO")
        # print("YES" if k%2 == 0 else "NO")
        pass