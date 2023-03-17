import sys
lines = list(map(str.strip, sys.stdin.readlines()))


def is_palindrome(s):
    n = len(s)
    left_hash, right_hash = 0, 0
    left_power, right_power = 1, 1
    base, mod = 128, 10**9 + 7  # base and mod values for rolling hash
    for i in range(n):
        # Update the rolling hash for the left substring and right reversed substring
        left_hash = (left_hash * base + ord(s[i])) % mod
        right_hash = (right_hash + ord(s[i]) * right_power) % mod
        left_power = (left_power * base) % mod
        right_power = (right_power * base) % mod

        # Compare the hashes for the left and right reversed substrings
        if left_hash == right_hash:
            print(f"The prefix '{s[:i+1]}' is a palindrome")

for line in lines[2::2]:
    s = line
    opened = 0
    n = len(s)
    removals = 0
    last_removed = 0
    good_so_far = True
    left_hash, right_hash = 0, 0
    left_power, right_power = 1, 1
    base, mod = 128, 10**9 + 7  # base and mod values for rolling hash
    for i, c in enumerate(s):
        left_hash = (left_hash * base + ord(s[i])) % mod
        right_hash = (right_hash + ord(s[i]) * right_power) % mod
        left_power = (left_power * base) % mod
        right_power = (right_power * base) % mod
        if left_hash == right_hash and i - last_removed > 0:
            if s[last_removed:i+1] == s[last_removed:i+1][::-1]:
                # Reset our hashes
                left_hash, right_hash = 0, 0
                left_power, right_power = 1, 1
                removals += 1
                last_removed = i + 1
                good_so_far = True
                opened += 1 if c == '(' else -1
                continue
        if c == '(':
            opened += 1
        elif c == ')':
            opened -= 1
            if opened == 0 and good_so_far:
                # Reset our hashes
                left_hash, right_hash = 0, 0
                left_power, right_power = 1, 1
                removals += 1
                last_removed = i + 1
            if opened < 0:
                good_so_far = False
    print(removals, n - last_removed)