import sys
lines = list(map(str.strip, sys.stdin.readlines()))

import math
N = 10**5 + 100
# stores smallest prime factor for every number
spf = [0 for i in range(N)]
def sieve():
    spf[1] = 1
    for i in range(2, N):
        spf[i] = i
    for i in range(4, N, 2):
        spf[i] = 2
    for i in range(3, math.ceil(math.sqrt(N))):
        # Is i prime=
        if (spf[i] == i):
            # in that case, mark the spf of all numbers divisible by i as i
            # (But only mark them if they have not previously been marked by a smaller number)
            for j in range(i * i, N, i):
                spf[j] = i if spf[j] == j else spf[j]
sieve()

# Very quickly finds the prime factors, since we always know what the
# next one is.
def prime_factors(x):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x //= spf[x]
    return ret

class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordcount = 0
        self.id = 0

def insert(word: list[int], root: TrieNode):
    curr = root
    for c in word:
        if c not in curr.children:
            curr.children[c] = TrieNode()
        curr = curr.children[c]
    curr.wordcount += 1

def amount_in_trie(word: list[int], root: TrieNode) -> bool:
    def dfs(i, curr):
        total = curr.wordcount
        for c in curr.children:
            for j in range(i, len(word)):
                if word[j] == c:
                    total += dfs(j + 1, curr.children[c])
                    break
        return total
    return dfs(0, root)

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    n = len(nums)
    nums = [x for x in nums if x <= n]
    trie_root = TrieNode()
    for x in nums:
        insert(prime_factors(x), trie_root)
    result = 0
    for i in range(1, n + 1):
        result = max(result, amount_in_trie(prime_factors(i), trie_root))
    print(result)
    
        