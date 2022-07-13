import sys
lines = list(map(str.strip, sys.stdin.readlines()))

# if mins or hrs < 10 we need to add a 0 in front
for line in lines[1:]:
    timesseen = set() # Make sure that we don't keep going too long
    time, interval = line.split(" ")
    hrs, mins = map(int, time.split(":"))
    minperinterval = int(interval) % 60
    hrperinterval = int(interval) // 60
    result = 0
    while True:
        hrsstring = str(hrs)
        if hrs < 10:
            hrsstring = '0' + hrsstring
        minsstring = str(mins)
        if mins < 10:
            minsstring = '0' + minsstring
        currtime = hrsstring + ":" +  minsstring
        if currtime in timesseen:
            break
        timesseen.add(currtime)
        # print(hrs, mins)
        # print(currtime)
        if currtime[::-1] == currtime:
            result += 1
        hrs = hrs + hrperinterval
        if mins + minperinterval >= 60:
            hrs += 1
        mins = (mins + minperinterval) % 60
        hrs %= 24
    # print("00:00" in timesseen)
    print(result)