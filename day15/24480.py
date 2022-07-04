from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, r = map(int, sys.stdin.readline().split())
node = list(list() for _ in range(n+1))
res = [0]*(n+1)

for i in range(m):
    s, e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)

cnt = 1
def DFS(v):
    global cnt
    res[v] = cnt
    node[v].sort(reverse=True)
    for i in node[v]:
        if res[i] == 0:
            cnt +=1
            DFS(i)
DFS(r)
for i in range(1, n+1):
    print(res[i])