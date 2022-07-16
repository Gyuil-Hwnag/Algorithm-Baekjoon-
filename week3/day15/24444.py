import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
node = list(list() for _ in range(n+1))
res = [0]*(n+1)

for i in range(m):
    s, e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)

for i in range(1, n+1):
    node[i].sort()

dQ = deque()
dQ.append(r)

cnt = 2
res[r] = 1
while dQ:
    tmp = dQ.popleft()
    for e in node[tmp]:
        if res[e] == 0:
            dQ.append(e)
            res[e] = cnt
            cnt+=1

for i in res[1:]:
    print(i)