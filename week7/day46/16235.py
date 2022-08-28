import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

board = [[5] * n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

def ADD():
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] <= board[i][j]:
                    board[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    for _ in range(k, len(trees[i][j])):
                        board[i][j] += trees[i][j].pop() // 2
                    break


def SUBMIT():
    for x in range(n):
        for y in range(n):
            for k in range(len(trees[x][y])):
                if trees[x][y][k] % 5 == 0:
                    for d in range(8):
                        xx, yy, = x + dx[d], y + dy[d]
                        if 0 <=xx<n and 0<=yy<n:
                            trees[xx][yy].appendleft(1)
            board[x][y] += a[x][y]

for _ in range(k):
    ADD()
    SUBMIT()

res = 0
for i in range(n):
    for j in range(n):
        res += len(trees[i][j])

print(res)