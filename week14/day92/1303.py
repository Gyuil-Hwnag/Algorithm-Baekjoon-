## 1303
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, -1, 0, 1, 0]
dy = [0, 0, -1, 0, 1]

def bfs(x, y, target):
    dq = deque([(x, y)])
    cnt = 0
    while dq:
        x, y = dq.popleft()
        for i in range(5):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<M and 0<=yy<N:
                if graph[xx][yy] == target and not visited[xx][yy]:
                    dq.append((xx, yy))
                    cnt += 1
                    visited[xx][yy] = True
    return cnt

N, M = map(int, input().split())
graph = list()
visited = [[False for _ in range(N)] for _ in range(M)]
for _ in range(M):
    graph.append(list(input().rstrip()))

B, W = 0, 0
for i in range(M):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 'W':
            resW = bfs(i, j, 'W')
            W = W + (resW**2)
        if not visited[i][j] and graph[i][j] == 'B':
            resB = bfs(i, j, 'B')
            B = B + (resB**2)

print(W, B)