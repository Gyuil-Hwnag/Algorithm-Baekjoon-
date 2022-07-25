import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

r, c, d = map(int, input().split())
board = list()
for i in range(n):
    board.append(list(map(int, input().split())))

def turn():
    global d
    d = (d-1)%4

y, x = r, c
board[y][x] = 2
cnt = 1

while True:
    check = False
    for _ in range(4):
        turn()
        xx = x+dx[d]
        yy = y+dy[d]
        if 0<=yy<n and 0<=xx<m: 
            if board[yy][xx] == 0:
                cnt += 1
                board[yy][xx] = 2
                x, y = xx, yy
                check = True
                break
    if not check: 
        xx = x-dx[d]
        yy = y-dy[d]
        if 0<=yy<n and 0<=xx<m:
            if board[yy][xx] == 2:
                x, y = xx, yy
            elif board[yy][xx] == 1:
                print(cnt)
                break
        else:
            print(cnt)
            break