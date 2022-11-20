import sys, math
def outerTrees(trees):
    def getvec(a, b): # Get the vector from a to b
        return [b[0] - a[0], b[1] - a[1]]
    def lenvec(v): # Get the length of a vector
        return math.sqrt(v[0]**2 + v[1]**2)
    def angle(a, b): # Get the angle between two vectors
        dp = (a[0] * b[0]) + (b[1] * a[1])
        lena = lenvec(a) 
        lenb = lenvec(b)
        print(dp, lena, lenb, lena*lenb)
        division = dp / (lena*lenb)
        if division < -1:
            division = -1
        if division > 1:
            division = 1
        return math.acos(division)
    def cp(a, b):
        return (a[0] * b[1]) - (b[0] * a[1])
    curr = min(trees, key=lambda x: x[1])
    result = set([tuple(curr)])
    spinningvec = [1, 0]
    while True:
        # print("Curr is", curr)
        smallest = [10**9, -1, None] # angle, index, The vector to that one
        for i in range(len(trees)):
            if trees[i] != curr:
                print("Checking angle between", curr, trees[i])
                v = getvec(curr, trees[i])
                print("Vectors", v, spinningvec)
                print("Point", trees[i])
                a = angle(spinningvec, v)
                print("Cross product", cp(v, spinningvec))
                print("Angle", a)
                print()
                if cp(v, spinningvec) > 0: continue
                if a == smallest[0]:
                    if lenvec(smallest[2]) > lenvec(v):
                        smallest = [a, i, v]
                elif a < smallest[0]:
                    smallest = [a, i, v]
        tup = tuple(trees[smallest[1]])
        # print(smallest)
        if tup in result: break
        result.add(tup)
        curr = trees[smallest[1]]
        spinningvec = smallest[2]                        
    return list(map(list, list(result)))
assert(outerTrees([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]) == [[2,4],[1,1],[2,0],[4,2],[3,3]])
print(outerTrees([[0,8],[9,8],[2,4]]))