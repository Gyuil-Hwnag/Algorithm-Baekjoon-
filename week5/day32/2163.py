import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

n, m = map(int, input().split())
ch = [[0]*m for _ in range(n)]

dQ = deque()
dQ.append((0, 0))

ch[0][0] = 1
cnt = 0

while dQ:
    x, y = dQ.popleft()
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<m and 0<=yy<n:
            if ch[yy][xx] == 0:
                ch[yy][xx] = 1
                dQ.append((xx, yy))
                cnt+=1

print(cnt)