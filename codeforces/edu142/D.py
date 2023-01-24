import sys
lines = list(map(str.strip, sys.stdin.readlines()))

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.children = {}
        self.count = 0

def insert(word: str, root: TrieNode):
    curr = root
    for c in word:
        if c not in curr.children:
            curr.children[c] = TrieNode()
        curr = curr.children[c]
        curr.count += 1
        curr.isWord = True
    curr.isWord = True

def in_trie(word: str, root: TrieNode) -> bool:
    curr = root
    for c in word:
        if c not in curr.children:
            return False
        curr = curr.children[c]
    return True

def permutation_product(p, q):
    n = len(p)
    product = [0] * n
    for o in range(n):
        product[o] = q[p[o]-1]
    return product

def beauty(arr):
    result = 0
    for o in range(len(arr)):
        if arr[o] == o + 1:
            result += 1
        else:
            break
    return result

def find_wanted(xs):
    result = [-1]*len(xs)
    for i in range(len(xs)):
        result[xs[i] - 1] = i + 1
    for x in range(len(result)):
        if result[x] == 10:
            result[x] = 0
        result[x] = str(result[x])
    return ''.join(result)

o = 1
while o < len(lines):
    n, m = map(int, lines[o].split())
    arrays = []
    for j in range(n):
        arrays.append(list(map(int, lines[o + j + 1].split())))
    root = TrieNode()
    for i in range(len(arrays)):
        to_insert = ""
        for j in range(len(arrays[i])):
            if arrays[i][j] == 10:
                to_insert += "0"
            else:
                to_insert += str(arrays[i][j])
        insert(to_insert, root)
    for i in range(len(arrays)):
        wanted = find_wanted(arrays[i])
        # print(arrays[i], wanted)
        curr = ""
        result = 0
        for c in wanted:
            curr += c
            if in_trie(curr, root):
                # print("string", curr, "in trie")
                result += 1
            else:
                # print("string", curr, "not in trie, breaking")
                break
        print(result, end=" ")
    print()
    o += n + 1
    # break
            
