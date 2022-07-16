import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

res = list()

def BFS(x, y):
    dQ = deque()
    dQ.append([x, y])
    farm[y][x] = -1

    while dQ:
        x, y = dQ.popleft()
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<m and 0<=yy<n:
                if farm[yy][xx]==1:
                    farm[yy][xx]=-1
                    dQ.append((xx, yy))
    return

for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    farm = list([0]*m for _ in range(n))

    for i in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                BFS(j, i)
                cnt+=1
    res.append(cnt)

for i in res:
    print(i)