import sys
lines = list(map(str.strip, sys.stdin.readlines()))


i = 1
while i < len(lines):
    n = int(lines[i])
    i+=1
    words = []
    while n > 0:
        words.append(lines[i])
        n-=1
        i+=1
    result = 0
    for char in ['a','b', 'c', 'd', 'e']:
        # print("current char", char)
        wordscopy = words.copy()
        for j in range(len(words)):
            wordscopy[j] = sum([1 if c == char else -1 for c in words[j]])
        total = 0
        wordscopy.sort(key=lambda x: -x)
        # print(wordscopy)
        for k in range(len(wordscopy)):
            total += wordscopy[k]
            if total <= 0:
                result = max(k, result)
                break
        if total > 0 and wordscopy[0] != 0:
            result = len(words)
            
    print(result) 