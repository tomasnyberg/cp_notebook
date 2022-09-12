import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    i = len(line) - 1
    result = ""
    while i >= 0:
        if line[i] == '0':
            # print(line[i-2:i])
            result += chr(int(line[i-2:i]) + 96) + ""
            i -= 3
        else:
            # print("curr", line[i], chr(int(line[i]) + 97))
            result += chr(int(line[i]) + 96)+ ""
            i-=1
    print(result[::-1])