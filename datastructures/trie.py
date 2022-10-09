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

def in_trie(word: str, root: TrieNode) -> bool:
    curr = root
    for c in word:
        if c not in curr.children:
            return False
        curr = curr.children[c]
    return curr.isWord
