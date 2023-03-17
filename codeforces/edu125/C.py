import sys
lines = list(map(str.strip, sys.stdin.readlines()))


class RollingPalindromeChecker:
    def __init__(self, base=131, mod=1_000_000_007):
        self.base = base
        self.mod = mod
        self.left_hash = 0
        self.right_hash = 0
        self.power = 1
        self.sequence = []

    def add_bit(self, bit):
        self.sequence.append(bit)
        self.left_hash = (self.left_hash * self.base + bit) % self.mod
        self.right_hash = (self.right_hash + self.power * bit) % self.mod
        self.power = (self.power * self.base) % self.mod

    def is_palindromic(self):
        return self.left_hash == self.right_hash and len(self.sequence) > 1


for line in lines[2::2]:
    s = list(map(int, (list(map(lambda x: '1' if x == '(' else '0', line)))))
    # print(s)
    opened = 0
    n = len(s)
    removals = 0
    last_removed = 0
    st = []
    pc = RollingPalindromeChecker()
    for i, c in enumerate(s):
        opened += 1 if c == 1 else -1
        pc.add_bit(c)
        if opened < 0: st.append([2])
        if st and st[-1] == 1 - c:
            st.pop()
        else:
            st.append(c)
        if not st or pc.is_palindromic():
            if st and pc.is_palindromic():
                if not s[last_removed:i+1] == s[last_removed:i+1][::-1]:
                    continue
            # print("Found good sequence", s[last_removed:i+1])
            st = []
            removals += 1
            last_removed = i + 1
            pc = RollingPalindromeChecker()
    print(removals, n - last_removed)
