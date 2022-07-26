import sys
lines = list(map(str.strip, sys.stdin.readlines()))


def solve(s, t):
    a = 0
    bs_needed = 0
    cs_needed = 0
    for a in range(0, len(s)):
        # print("start" ,a, bs_needed, cs_needed)
        schar = chr(s[a])
        tchar = chr(t[a])
        # In the case that we are trying to find chars to shift back, don't look at anything else
        if bs_needed > 0 or cs_needed > 0:
            # If we are trying to find bs to shift back and we encounter a c,
            # Or conversely, we are trying to find cs to shift back and we encounter an a.
            # In both of these cases, we cannot shift the chars we want back.
            if schar == 'c' and bs_needed > 0 or schar == 'a' and cs_needed > 0:
                print("NO")
                return
            if bs_needed > 0 and tchar == 'b':
                bs_needed += 1
            if bs_needed > 0 and schar == 'b':
                bs_needed -= 1
            if cs_needed > 0 and tchar == 'c':
                cs_needed +=1
            if cs_needed > 0 and schar == 'c':
                cs_needed -= 1
            continue
        if schar != tchar: # Set up our bs_needed or our cs_needed to be correct
            # In both of these cases there is no way we can continue (i think)
            if s[a] > t[a] or schar == 'a' and tchar == 'c':
                print("NO")
                return
            if schar == 'a' and tchar == 'b':
                bs_needed = 1
            else:
                cs_needed = 1
        # print("end" , a, bs_needed, cs_needed)
    if bs_needed == 0 and cs_needed == 0:
        print("YES")
    else:
        print("NO")

for i in range(2, len(lines), 3):
    s = list(map(ord, lines[i]))
    t = list(map(ord, lines[i+1]))
    solve(s, t) 