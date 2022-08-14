import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    # Maintain a dict of the amount of all numbers in the nums array
    counts = {}
    for num in nums:
        counts[num] = 1 if num not in counts else counts[num] + 1
    stack = [] # Our "extra" numbers, the ones we can use to fill in the ones we don't have
    bad = False # If we couldn't find the previous, we can't find the next either
    sum = 0 # Sum of the changes we had to make so far to get the next MEX
    for i in range(len(nums)+1):
        if bad:
            print(-1, end=" ")
            continue
        # If the previous number is not in nums we need to add it
        # we do this by getting the biggest available num (top of stack since that is in increasing order)
        # then adding to that number until it is equal to i-1, i.e. we need to add (i-1) - biggest
        # To get the next MEX. The next MEX after i will also have to add all the previous ones so 
        # Maintain a sum of what we have had to add so far.
        # If the stack is empty the array is bad and everything after it will be bad
        if i > 0 and i-1 not in counts:
            if not stack:
                bad = True
                print(-1, end=" ")
                continue
            biggest = stack.pop()
            sum += i - 1 - biggest
        # We also need to remove all the current occurences of i to make it MEX, so add
        # counts[i] if it is in counts
        print(sum + (counts[i] if i in counts else 0), end=" ")
        # Add all the occurrences of this num to the stack except for 1.
        # The one that is left will be the one used in all the next MEXes
        while i in counts and counts[i] > 1:
            stack.append(i)
            counts[i]-=1
    print()