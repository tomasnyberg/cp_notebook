import math
import random


class sparse_table:
    def __init__(self, array, func=min):
        self.array = array
        self.size = len(array)
        self.func = func
        self.sparse_table = self.build_sparse_table()

    def build_sparse_table(self):
        sparse_table = [self.array]
        for j in range(1, int(math.log2(self.size)) + 1):
            prev_row = sparse_table[j - 1]
            curr_row = []
            for i in range(self.size):
                if i + (1 << j) > self.size:
                    break
                curr_row.append(
                    self.func(prev_row[i], prev_row[i + (1 << (j - 1))]))
            sparse_table.append(curr_row)
        return sparse_table

    def query(self, left, right):
        j = int(math.log2(right - left + 1))
        return self.func(self.sparse_table[j][left], self.sparse_table[j][right - (1 << j) + 1])


def test():
    numbers = [random.randint(0, 100) for _ in range(10000)]
    st = sparse_table(numbers)
    stmax = sparse_table(numbers, func=max)
    for i in range(100000):
        left = random.randint(0, len(numbers) - 1)
        right = random.randint(left, len(numbers) - 1)
        assert st.query(left, right) == min(numbers[left:right + 1])
        assert stmax.query(left, right) == max(numbers[left:right + 1])
    print("Passed tests")

test()
