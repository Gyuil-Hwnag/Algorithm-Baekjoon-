## 6118
import sys
from collections import deque
input = sys.stdin.readline

def bfs(target):
    dq = deque()
    dq.append(target)
    visited[target] = 1
    while dq:
        target = dq.popleft()
        for next in graph[target]:
            if visited[next] == 0:
                visited[next] = visited[target]+1
                dq.append(next)

res = 0
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
res = max(visited)
print(visited.index(res), res-1, visited.count(res))
