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
    num = ""
    while i >= 0 and stringed[i] != '0':
        num += stringed[i]
        i-=1
    # print(num)
    num = int(num[::-1])
    multiplier = 1
    result = -1
    timesmultid = 0
    while True:
        i = 2
        while i < 11:
            if (num * i) % 10 == 0:
                multiplier *= i
                timesmultid += 1
                num = (num*i) // 10
                break
            i+=1
        if multiplier > m:
            if timesmultid == 1:
                break
            multiplier //= i
            result = multiplier
            # print("Stop at", multiplier)
            for k in range(2, 11):
                if multiplier * k <= m:
                    result = multiplier * k
            break
    if result == -1:
        print(n*m)
        continue
    print(n*result)

                


        
        
    