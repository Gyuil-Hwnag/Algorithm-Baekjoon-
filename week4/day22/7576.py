import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
miro = list(list(map(int ,input().split())) for _ in range(n))
dQ = deque()

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for i in range(n):
    for j in range(m):
        if miro[i][j]==1:
            dQ.append((j, i))
        
while dQ:
    x, y = dQ.popleft()
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        # print("%d %d" %(xx, yy))
        if 0<=xx<m and 0<=yy<n:
            if miro[yy][xx] == 0:
                miro[yy][xx] = miro[y][x]+1
                dQ.append((xx, yy))

res = 0
for i in miro:
    for j in i:
        if res<j:
            res = j
        if j==0:
            print(-1)
            exit(0)
else:
    print(res-1)