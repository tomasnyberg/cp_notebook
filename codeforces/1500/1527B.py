import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from functools import lru_cache

# lines = """2
# 4
# 1001
# 1
# 0
# 5
# 10010""".split("\n")

for s in lines[2::2]:
    if len(s) % 2 == 1 and s[len(s) // 2] == '0' and len(s) > 1:
        print("ALICE")
    else:
        print("BOB")
    # non_palindrome_zeroes = []
    # for i in range(len(s) // 2):
    #     if s[i] != s[len(s) - i - 1] and s[i] == '0':
    #         non_palindrome_zeroes.add(i)
    # palindrome_zeroes = [i for i in range(len(s)) if i not in non_palindrome_zeroes and s[i] == '0']
    # middle_element = len(s) % 2 == 1 and s[len(s) // 2] == '0'
    # if len(s) % 2 == 1 and s[len(s) // 2] == '0':
    #     non_palindrome_zeroes.pop(len(s) // 2) # Remove the middle element from the
    # paid = 0
    # turn = 1
    # total = sum([int(i) for i in s])
    # reversed_previous = False
    # while total < len(s):
    #     turn = 1 - turn
    #     if non_palindrome_zeroes and not reversed_previous:
    #         reversed_previous = True
    #         continue


        





