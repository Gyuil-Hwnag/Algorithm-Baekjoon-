import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
dQ = deque()
dy = [0]*100001
dQ.append(n)

while dQ:
    x = dQ.popleft()
    if x==k:
        break
    else:
        for i in (x-1, x+1, x*2):
            if 0<=i<=100000 and dy[i]==0:
                dy[i] = dy[x]+1
                dQ.append(i)

print(dy[k])