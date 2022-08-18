import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from heapq import heappush, heappop

customercount = 1
hqbytime = []
hqbymoney = []
served = set()
# We might have to specially handle the case where polycarp serves so that he serves the one that came in first
for line in lines[1:]:
    if line[0] == '1':
        _, money = map(int, line.split(" "))
        heappush(hqbymoney, (-money, customercount))
        heappush(hqbytime, customercount)
        customercount += 1
    if line[0] == '2':
        customer = heappop(hqbytime)
        while customer in served:
            customer = heappop(hqbytime)
        # print("monocarp serves customer", customer)
        print(customer, end=" ")
        served.add(customer) 
    if line[0] == '3':
        money, customer = heappop(hqbymoney)
        while customer in served:
            money, customer = heappop(hqbymoney)
        # print("polycarp serves customer", customer)
        print(customer,end =" ")
        served.add(customer)
print()

