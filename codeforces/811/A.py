import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
while i < len(lines):
    n, H, M = map(int, lines[i].split(" "))
    smallesthdiff = 24
    alarms = []
    i+=1
    while n > 0:
        alarms.append(list(map(int, lines[i].split(" "))))
        n-=1
        i+=1
    # print(alarms)
    for j in range(len(alarms)):
        hour, minute = alarms[j]
        if hour > H:
            hourdiff = hour - H
            minutediff = -1
            if minute >= M:
                minutediff = minute - M
            else:
                hourdiff -=1
                minutediff = 60-M+minute
            alarms[j] = [hourdiff, minutediff]
        elif hour == H:
            if minute >= M:
                alarms[j] = [0, minute - M]
            else:
                alarms[j] = [23, 60 - M + minute]
        else:
            hourdiff = 24 - H + hour
            if minute >= M:
                alarms[j] = [hourdiff, minute - M]
            else:
                hourdiff -= 1
                alarms[j] = [hourdiff, 60 - M + minute]
    smallesthdiff = 25
    for hour, minute in alarms:
        smallesthdiff = min(smallesthdiff, hour)
    smallestmindiff = 61
    for hour, minute in alarms:
        if hour == smallesthdiff:
            smallestmindiff = min(smallestmindiff, minute)
    print(smallesthdiff, smallestmindiff)