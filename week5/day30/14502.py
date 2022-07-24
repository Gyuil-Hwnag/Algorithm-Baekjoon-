import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
n, m = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def BFS():
    global res
    ch = deepcopy(board)

    virus = deque()
    for i in range(n):
        for j in range(m):
            if ch[i][j] == 2:
                virus.append((j, i))

    # for i in ch:
    #     print(i)
    while virus:
        x, y = virus.popleft()
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            # print("%d %d %d %d" %(xx, yy, m, n))
            if 0<=xx<m and 0<=yy<n:
                if ch[yy][xx] == 0:
                    ch[yy][xx] = 2
                    virus.append((xx, yy))
    # for i in ch:
    #     print(i)
    cnt = 0
    for i in ch:
        for j in i:
            if j==0:
                cnt+=1
    res = max(cnt, res)

def ADD(cnt):
    if cnt==3:
        BFS()
        return
    else:
        for y in range(n):
            for x in range(m):
                if board[y][x] == 0:
                    board[y][x] = 1
                    ADD(cnt+1)
                    board[y][x] = 0

res = 0
ADD(0)
print(res)