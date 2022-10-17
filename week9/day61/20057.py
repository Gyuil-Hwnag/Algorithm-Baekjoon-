import sys
input = sys.stdin.readline

ty = [
    [-1, -1, -1, 1, 1, 1, -2, 2, 0],
    [-1, 0, 1, -1, 0, 1, 0, 0, 2],
    [-1, -1, -1, 1, 1, 1, -2, 2, 0],
    [-1, 0, 1, -1, 0, 1, 0, 0, -2],
]

tx = [
    [-1, 0, 1, -1, 0, 1, 0, 0, -2],
    [-1, -1, -1, 1, 1, 1, -2, 2, 0],
    [-1, 0, 1, -1, 0, 1, 0, 0, 2],
    [-1, -1, -1, 1, 1, 1, -2, 2, 0],
]

ratio = [
    [0.1, 0.07, 0.01, 0.1, 0.07, 0.01, 0.02, 0.02, 0.05],
    [0.01, 0.07, 0.1, 0.01, 0.07, 0.1, 0.02, 0.02, 0.05],
    [0.01, 0.07, 0.1, 0.01, 0.07, 0.1, 0.02, 0.02, 0.05],
    [0.1, 0.07, 0.01, 0.1, 0.07, 0.01, 0.02, 0.02, 0.05],
]

def check_range(y, x):
    return (0<=y<n) and (0<=x<n)

def tornado(y, x, d, board):
    global res
    m = board[y][x]
    board[y][x] = 0
    total = 0
    for i in range(9):
        ny = y + ty[d][i]
        nx = x + tx[d][i]
        r = ratio[d][i]
        if check_range(ny, nx):
            board[ny][nx] += int((m*r))
            total += int((m*r))
        else:
            res += int((m*r))
            total += int((m*r))

    ny = y+dy[d]
    nx = x+dx[d]
    if check_range(ny, nx):
        board[ny][nx] += (m-total) if m-total>0 else 0
    else:
        res += (m - total) if m - total > 0 else 0

    return board

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

res = 0
number = 0
cy, cx, cd = n//2, n//2, 0
cnt, total = 0, 1

while number<n**2:
    if cnt==total:
        cnt = 0
        cd = (cd+1)%4
        if cd==0 or cd==2:
            total+=1

    cy+=dy[cd]
    cx+=dx[cd]

    number+=1
    cnt+=1
    if board[cy][cx] > 0:
        board = tornado(cy, cx, cd, board)

print(res)