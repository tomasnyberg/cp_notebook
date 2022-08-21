def nPr(n, r):
    import math
    return math.factorial(n) // math.factorial(n-r)

def nCr(n,r):
    import math
    return math.factorial(n) // (math.factorial(r)*(math.factorial(n-r)))
