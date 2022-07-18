import sys
input = sys.stdin.readline
from collections import deque

def BFS(s):
    visited[s]=1
    q = deque()
    q.append(s)
    while q:
        a = q.popleft()
        for i in dQ[a]:
            if visited[i]==0:
                visited[i] = -visited[a]
                q.append(i)
            else:
                if visited[i] == visited[a]:
                    return False
    return True

k = int(input())
for i in range(k):
    v, e = map(int, input().split())
    dQ = [[] for _ in range(v+1)]
    visited = [0]*(v+1)
    res = True
    for j in range(e):
        a, b = map(int, input().split())
        dQ[a].append(b)
        dQ[b].append(a)
    for k in range(1, v+1):
        if visited[k]==0:
            if not BFS(k):
                res = False
                break
    
    if res:
        print("YES")
    else:
        print("NO")