import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dQ = deque()

res = list()
dQ.append(0)
def Remove():
    if len(dQ) == 2:
        res.append(dQ.pop())
    elif len(dQ) < 2:
        res.append(0)
    else:
        dQ.popleft()
        res.append(dQ.popleft())
        dQ.appendleft(dQ.pop())
        dQ.appendleft(0)
        n = 1
        while n<len(dQ)-1:
            if len(dQ) > n*2+1:
                if dQ[n] < dQ[n*2]:
                    dQ[n*2], dQ[n] = dQ[n], dQ[n*2]
                    n = n*2
                else:
                    if dQ[n] < dQ[n*2+1]:
                        dQ[n*2+1], dQ[n] = dQ[n], dQ[n*2+1]
                        n = n*2+1
            elif len(dQ) > n*2:
                if dQ[n] < dQ[n*2]:
                    dQ[n*2], dQ[n] = dQ[n], dQ[n*2]
                    n = n*2
            # print(dQ)
            n = n*2
    # print(dQ)

def Insert(L):
    dQ.append(L)
    n = len(dQ)-1
    while n>1:
        if dQ[n//2] < dQ[n]:
            dQ[n//2], dQ[n] = dQ[n], dQ[n//2]
        n = n//2

for i in range(n):
    s = int(input())
    if s==0:
        Remove()
    else:
        Insert(s)

for i in res:
    print(i)