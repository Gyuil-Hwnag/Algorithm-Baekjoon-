from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
v = int(input())
node = list(list() for _ in range(n+1))
dy = [0]*(n+1)

for i in range(v):
    s, e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)

cnt = 0
def DFS(L):
    global cnt
    dy[L] = 1
    for i in node[L]:
        if dy[i] == 0:
            DFS(i)
            cnt+=1

DFS(1)
print(cnt)