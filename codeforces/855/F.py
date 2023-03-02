import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from functools import lru_cache

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 0

def insert(word: str, root: TrieNode, ii):
    curr = root
    for idx, c in enumerate(word):
        j = int(c)
        if not curr.children[j]:
            curr.children[j] = TrieNode()
        curr = curr.children[j]
    curr.count += 1

def amount_in_trie(word: str, root: TrieNode):
    curr = root
    for c in word:
        j = int(c)
        if not curr.children[j]:
            return 0
        curr = curr.children[j]
    return curr.count

oddroot = TrieNode()
evenroot = TrieNode()

for idx, line in enumerate(lines[1:]):
    num = 0
    for c in line:
        num ^= 1 << (ord(c) - ord('a'))
    s = bin(num)[2:]
    s = '0' * (26 - len(s)) + s
    if len(line) % 2 == 0:
        insert(s, evenroot, idx)
    else:
        insert(s, oddroot, idx)

result = 0
for ii, line in enumerate(lines[1:]):
    num = 0
    for c in line:
        num ^= 1 << (ord(c) - ord('a'))
    s = bin(num)[2:]
    s = '0' * (26 - len(s)) + s
    lookingfor = ""
    for c in s:
        if c == '0':
            lookingfor += '1'
        else:
            lookingfor += '0'
    lookingfor = list(lookingfor)
    possibilities = []
    for idx, c in enumerate(lookingfor):
        if c == '1':
            lookingfor[idx] = '0'
            possibilities.append(''.join(lookingfor))
            lookingfor[idx] = '1'
    matches = 0
    if len(line) % 2 == 0:
        for possibility in possibilities:
            matches += amount_in_trie(possibility, oddroot)
    else:
        for possibility in possibilities:
            matches += amount_in_trie(possibility, evenroot)
    result += matches
    # print("line", s, "can contribute with", matches)
print(result//2)