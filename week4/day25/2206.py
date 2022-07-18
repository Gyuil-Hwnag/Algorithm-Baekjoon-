from itertools import count
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
miro = list()
ch = [[[0] * 2 for _ in range(m)] for _ in range(n)]
for i in range(n):
    s = list(input().strip())
    for j in range(m):
        s[j] = int(s[j])
    miro.append(s)
# print(miro)

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

dQ = deque()
dQ.append((0, 0, 0))
ch[0][0][0] = 1
res = n*m
while dQ:
    # print(dQ)
    x, y, cnt = dQ.popleft()
    if x==m-1 and y==n-1:
        print(ch[y][x][cnt])
        break
    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<m and 0<=yy<n:
                if miro[yy][xx]==1 and cnt==0:
                    ch[yy][xx][1] = ch[y][x][0] + 1
                    dQ.append((xx, yy, 1))
                if miro[yy][xx]==0 and ch[yy][xx][cnt] == 0:
                    ch[yy][xx][cnt] = ch[y][x][cnt] + 1
                    dQ.append((xx, yy, cnt))
else:
    print(-1)