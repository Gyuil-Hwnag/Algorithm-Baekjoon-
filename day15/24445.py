from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
node = list(list() for _ in range(n+1))
dy = [0]*(n+1)

for i in range(m):
    s, e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)

for i in range(1, n+1):
    node[i].sort(reverse=True)

dQ = deque()
dQ.append(r)
dy[r] = 1
cnt=2
while dQ:
    tmp = dQ.popleft()
    for i in node[tmp]:
        if dy[i] == 0:
            dQ.append(i)
            dy[i] = cnt
            cnt+=1

for i in dy[1:]:
    print(i)