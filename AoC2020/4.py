import sys
lines = list(map(str.strip, sys.stdin.readlines()))

person = 0
result = 0
for line in lines:
    if not line:
        if person == 7:
            result += 1
        person = 0
        continue
    for s in line.split(" "):
        if s[:3] == "cid": 
            continue
        elif s[:3] == "byr":
            if 1920 <= int(s[4:]) <= 2002:
                person += 1
            else:
                print(s[3:], "byr")
        elif s[:3] == "iyr":
            if 2010 <= int(s[4:]) <= 2020:
                person += 1
            else:
                print(s[3:], "iyr")
        elif s[:3] == "eyr":
            if 2020 <= int(s[4:]) <= 2030:
                person += 1
            else:
                print(s[3:], "eyr")
        elif s[:3] == "hgt":
            if len(s[4:]) < 4 or not all(48 <= ord(c) <= 57 for c in s[4:-2]):
                print(s[4:], "hgt 1")
                continue
            num = int(s[4:-2])
            if s[-2] + s[-1] == "cm":
                if 150 <= num <= 193:
                    person += 1
                else:
                    print(s[3:], "hgt 2" )
            else:
                if 59 <= num <= 76:
                    person += 1
                else:
                    print(s[3:], "hgt 3")
        elif s[:3] == "hcl":
            if len(s[4:]) == 7 and s[4] == '#' and all(48 <= ord(c) <= 57 or 97 <= ord(c) <= 102 for c in s[5:]):
                person += 1
            else:
                print(s[3:], "hcl")
        elif s[:3] == "ecl":
            if s[4:] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                person += 1
            else:
                print(s[3:], "ecl")
        elif s[:3] == "pid":
            if len(s[4:]) == 9 and all(48<= ord(c) <= 57 for c in s[4:]):
                person += 1
            else:
                print(s[3:], "pid")
        else:
            print("fount no one at all")
        print(s, person)
        
print(result)


