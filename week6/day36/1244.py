import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

sw = deque(map(int, input().split()))
sw.appendleft(0)

def MAN(L):
    while L<=n:
        sw[L] = (sw[L]+1)%2
        L+=L
        
def WOMAN(L):
    i = 1
    while (L-i)>0 and (L+i)<n+1:
        if sw[L-i] != sw[L+i]:
            break
        i+=1
    if (L-i)>0 or (L+i)<n:
        for p in range(L-i, L+i):
            sw[p] = (sw[p]+1)%2
    else:
        for p in range(1, n+1):
            sw[p] = (sw[p]+1)%2

num = int(input())
for i in range(num):
    p, w = map(int, input().split())
    if p==1:
        MAN(w)
    elif p==2:
        WOMAN(w)

for i in range(1, n+1):
    print(sw[i], end=' ')