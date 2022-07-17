import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]

def BFS(sx, sy):
    dQ = deque()
    dQ.append((sx, sy, 0))
    res = 214700000
    while dQ:
        # print(dQ)
        x, y, t = dQ.popleft()
        if t>res:
            continue
        if x==ex and y==ey:
            if t<res:
                res=t

        for i in range(8):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<l and 0<=yy<l:
                if cheese[yy][xx] == 0:
                    cheese[yy][xx]=1
                    dQ.append((xx, yy, t+1))
    return res

r = list()
for i in range(t):
    l = int(input())
    cheese = list([0]*l for _ in range(l))
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    r.append(BFS(sx, sy))

for i in r:
    print(i)