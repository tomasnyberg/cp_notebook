import sys
lines = list(map(str.strip, sys.stdin.readlines()))

import math

class SparseTableMax:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.log_n = self._compute_log_n()
        self.table = self._build_table()

    def _compute_log_n(self):
        return (self.n - 1).bit_length()

    def _build_table(self):
        table = [[0] * self.log_n for _ in range(self.n)]
        for i in range(self.n):
            table[i][0] = self.arr[i]
        for j in range(1, self.log_n):
            for i in range(self.n - (1 << j) + 1):
                table[i][j] = max(table[i][j-1], table[i+(1<<(j-1))][j-1])
        return table

    def query(self, l, r):
        j = (r - l + 1).bit_length() - 1
        return max(self.table[l][j], self.table[r-(1<<j)+1][j])

class SparseTableMin:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.log_n = self._compute_log_n()
        self.table = self._build_table()

    def _compute_log_n(self):
        return (self.n - 1).bit_length()

    def _build_table(self):
        table = [[0] * self.log_n for _ in range(self.n)]
        for i in range(self.n):
            table[i][0] = self.arr[i]
        for j in range(1, self.log_n):
            for i in range(self.n - (1 << j) + 1):
                table[i][j] = min(table[i][j-1], table[i+(1<<(j-1))][j-1])
        return table

    def query(self, l, r):
        j = (r - l + 1).bit_length() - 1
        return min(self.table[l][j], self.table[r-(1<<j)+1][j])
    
# stmin = SparseTableMin([1,2,3,4,5,6,7,8,9,10])
# stmax = SparseTableMax([1,2,3,4,5,6,7,8,9,10])

# print(stmin.query(2, 9))
# print(stmax.query(2, 9))

i = 1
while i < len(lines):
    n = int(lines[i])
    a = []
    b = []
    i+=1
    for _ in range(n):
        x, y = map(int, lines[i].split())
        a.append(x)
        b.append(y)
        i+=1
    low = 0
    high = len(a) - 1
    def check(x):
        bmax = 0
        for i in range(len(a)):
            if a[i] >= x:
                bmax = max(bmax, b[i])
        return abs(x-bmax)
    ab = [(x,y) for x, y in zip(a, b)]
    ab.sort()
    a = [x for x, y in ab]
    b = [y for x, y in ab]
    stmin = SparseTableMin(b)
    stmax = SparseTableMax(b)
    result = 10**15
    for j in range(len(a) - 1):
        lower = abs(a[j] - stmin.query(j+1, len(a)-1))
        upper = abs(a[j] - stmax.query(j+1, len(a)-1))
        result = min(result, lower, upper)
    lower = abs(a[-1] - stmin.query(0, len(a)-2))
    upper = abs(a[-1] - stmax.query(0, len(a)-2))
    result = min(result, lower, upper)
    print(result)