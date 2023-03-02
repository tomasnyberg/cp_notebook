import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from functools import lru_cache

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.words = []
        self.children = {}
        self.count = 0

def insert(word: str, root: TrieNode, ii):
    curr = root
    for idx, c in enumerate(word):
        if c not in curr.children:
            curr.children[c] = TrieNode()
        curr = curr.children[c]
    curr.words.append(ii)

def amount_in_trie(word: str, root: TrieNode):
    curr = root
    for c in word:
        if c not in curr.children:
            return [] ## TODO we could possible be able to skip this character
        curr = curr.children[c]
    return curr.words

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

result = set()
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
    matches = []
    if len(line) % 2 == 0:
        for possibility in possibilities:
            matches += amount_in_trie(possibility, oddroot)
    else:
        for possibility in possibilities:
            matches += amount_in_trie(possibility, evenroot)
    for m in matches:
        t = (min(ii,m), max(ii, m))
        result.add(t)
    # print("line", s, "can contribute with", matches)
print(len(result))