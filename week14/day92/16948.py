## 16948
import sys
from collections import deque
input = sys.stdin.readline

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs(x, y):
    dq = deque([(x, y)])
    while dq:
        x, y = dq.popleft()
        for i in range(6):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<N and 0<=yy<N and visited[xx][yy] == 0:
                visited[xx][yy] = visited[x][y]+1
                if xx == r2 and yy == c2:
                    return visited[xx][yy]
                dq.append((xx, yy))

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[0 for _ in range(N)] for _ in range(N)]

res = bfs(r1, c1)
if res == None:
    print(-1)
else:
    print(res)