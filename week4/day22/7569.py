from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
miro = list(list(list(map(int ,input().split())) for _ in range(n)) for _ in range(h))

dz = [-1, 1]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
dQ = deque()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if miro[k][i][j]==1:
                dQ.append((j, i, k))

while dQ:
    x, y, z = dQ.popleft()
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<m and 0<=yy<n:
            if miro[z][yy][xx] == 0:
                miro[z][yy][xx] = miro[z][y][x]+1
                dQ.append((xx, yy, z))
    
    for i in range(2):
        zz = z+dz[i]
        if 0<=zz<h:
            if miro[zz][y][x] == 0:
                miro[zz][y][x] = miro[z][y][x]+1
                dQ.append((x, y, zz))

# print(miro)
res = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if miro[i][j][k] == 0:
                print(-1)
                exit(0)
            res = max(res, miro[i][j][k])
else:
    print(res-1)