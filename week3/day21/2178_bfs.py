import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
miro = list()
for i in range(n):
    num = list(str(input().rstrip()))
    for j in range(m):
        num[j] = int(num[j])
    miro.append(num)

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
res = n*m
dQ = deque()
dQ.append((0, 0))

def BFS():
    while dQ:
        x, y = dQ.popleft()
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<m and 0<=yy<n:
                if miro[yy][xx]==1:
                    miro[yy][xx] = miro[y][x]+1
                    dQ.append((xx, yy))
        
BFS()
print(miro[-1][-1])