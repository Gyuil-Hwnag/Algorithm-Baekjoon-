## 3184
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dq = deque([(x, y)])
    v = 0
    o = 0

    while dq:
        x, y = dq.popleft()
        for i in range(5):
            xx = x+dx[i]
            yy = y+dy[i]

            if 0<=xx<R and 0<=yy<C and not visited[xx][yy]:
                if graph[xx][yy] == '#':
                    continue
                elif graph[xx][yy] == 'v':
                    v += 1
                elif graph[xx][yy] == 'o':
                    o += 1
                dq.append((xx, yy))
                visited[xx][yy] = True
    return o, v

dx = [0, -1, 0, 1, 0]
dy = [0, 0, -1, 0, 1]
R, C = map(int, input().split())
graph = list()
visited = list([False for _ in range(C)] for _ in range(R))

for _ in range(R):
    graph.append(list(input().rstrip()))

sheep, wolf = 0, 0
for i in range(R):
    for j in range(C):
        if not visited[i][j] and graph[i][j] != '#':
            s, w = bfs(i, j)
            if s > w:
                sheep += s
            else:
                wolf += w
print(sheep, wolf)
            