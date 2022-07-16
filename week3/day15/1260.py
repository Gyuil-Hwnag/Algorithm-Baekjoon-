from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
node = list([] for _ in range(n+1))
dfs = [0]*(n+1)
bfs = [0]*(n+1)
for i in range(m):
    s, e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)

for i in range(n+1):
    node[i].sort()

resD = list()
dfs[v] = 1
def DFS(L):
    dfs[L] = 1
    resD.append(L)
    for e in node[L]:
        if dfs[e] == 0:
            DFS(e)
DFS(v)

dQ = deque()
dQ.append(v)
resB = list()
bfs[v] = 1
while dQ:
    tmp = dQ.popleft()
    resB.append(tmp)
    for i in node[tmp]:
        if bfs[i] == 0:
            bfs[i] = 1
            dQ.append(i)

for i in resD:
    print(i, end=' ')
print()
for i in resB:
    print(i, end=' ')