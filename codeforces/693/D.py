import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    odds = [x for x in nums if x % 2 == 1]
    evens = [x for x in nums if x % 2 == 0]
    odds.sort()
    evens.sort()
    alice = 0
    bob = 0
    i = 0
    while odds or evens:
        if i % 2 == 0: # Alice's turn
            o = odds[-1] if odds else 0
            e = evens[-1] if evens else 0
            if o > e:
                odds.pop() 
            else:
                alice += evens.pop()
        else:
            o = odds[-1] if odds else 0
            e = evens[-1] if evens else 0
            if o > e:
                bob += odds.pop() 
            else:
                evens.pop()
        i+=1
    if alice == bob:
        print("Tie")
    else:
        print("Alice" if alice > bob else "Bob")
    
