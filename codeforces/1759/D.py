import sys
lines = list(map(str.strip, sys.stdin.readlines()))

# best = [-1,-1]
# for i in range(1, m+1):
#     z = zeroes(n*i)
#     if z >= best[0]:
#         best = [z, i]
# print(n*best[1], "was best for", n, "(times)", best[1], "(max)", m)
def zeroes(x):
    stringed = str(x)
    result = 0
    for c in stringed[::-1]:
        if c != '0': break
        result += 1
    return result
        
for line in lines[1:]:
    n, m = map(int, line.split(" "))
    z = zeroes(n)
    stringed = str(n)
    i = len(stringed) - 1
    while stringed[i] == '0':
        i-=1
    num = int(stringed[i])
    multiplier = 1
    result = -1
    while True:
        i = 2
        while i < 11:
            if (num * i) % 10 == 0:
                multiplier *= i
                num = (num*i) // 10
                break
            i+=1
        if multiplier > m:
            multiplier //= i
            for i in range(2, 11):
                if multiplier * i < m:
                    result = multiplier * i
            break
    if result == -1:
        print(n*m)
        continue
    print(n*result)

                


        
        
    