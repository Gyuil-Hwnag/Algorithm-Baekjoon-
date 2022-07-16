import sys
from math import sqrt
input = sys.stdin.readline

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

num = list()
n = int(input())

for i in range(n):
    num.append(int(input()))

num.sort()
res = list()
gcdlist = list()

for i in range(1, n):
    gcdlist.append(num[i]-num[i-1])

prev = gcdlist[0]
for i in range(1, len(gcdlist)):
    prev = gcd(prev, gcdlist[i])

for i in range(2, int(sqrt(prev)) + 1):
    if prev % i == 0:
        res.append(i)
        res.append(prev//i)

res.append(prev)
res = list(set(res))
res.sort()

for i in res:
    print(i, end=' ')