# Given a stream of 1s and 0s, check if the sequence so far is longer than 1 and is a palindrome.
class rolling_palindrome_checker:
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