import sys

def handle_notfound(counter):
    print("?", counter, 1)
    sys.stdout.flush()
    if int(input()) == -1:
        return counter-1
    else:
        return counter


counter = 1
while(True):
    print("?", counter, counter+1)
    sys.stdout.flush()
    a = int(input())
    if a == 0: sys.exit(0)
    if a == -1:
        print("!", handle_notfound(counter))
        sys.exit(0)
    print("?", counter+1, counter)
    sys.stdout.flush()
    b = int(input())
    if a == b:
        counter += 2
    else:
        print("!", a+b)
        sys.exit(0)

