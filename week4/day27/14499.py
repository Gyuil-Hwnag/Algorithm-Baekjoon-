import sys
input = sys.stdin.readline

def MOVE(direction):
    if direction == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif direction == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif direction == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif direction == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m, x, y, k = map(int, input().split())
board = []

for i in range(n):
    board.append(list(map(int, input().split())))
move = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0, 0]
res = list()
for i in move:
    a, b = dx[i-1], dy[i-1]
    if 0<=x+a<n and 0<=y+b<m:
        x += a
        y += b
        MOVE(i)
        if board[x][y] != 0:
            dice[1] = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = dice[1]
        res.append(dice[6])
        # print(dice[6])

for i in res:
    print(i)