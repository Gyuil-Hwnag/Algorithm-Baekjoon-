import sys
input = sys.stdin.readline

R, C, m = map(int, input().split())
g = [[0] * C for i in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
res = 0

def MOVE():
    temp = [[0]*C for i in range(R)]
    for i in range(R):
        for j in range(C):
            if g[i][j] != 0:
                x, y, s, d, z = i, j, g[i][j][0], g[i][j][1], g[i][j][2]
                while s > 0:
                    x += dx[d]
                    y += dy[d]
                    if 0 <= x < R and 0 <= y < C:
                        s -= 1
                    else:
                        x -= dx[d]
                        y -= dy[d]
                        if d == 0: d = 1
                        elif d == 1: d = 0
                        elif d == 2: d = 3
                        elif d == 3: d = 2
                if temp[x][y] == 0:
                    temp[x][y] = [g[i][j][0], d, z]
                else:
                    if temp[x][y][2] < z:
                        temp[x][y] = [g[i][j][0], d, z]
    return temp

for i in range(1, m+1):
    r, c, s, d, z = map(int, input().split())
    g[r-1][c-1] = [s, d-1, z]

for i in range(C):
    for j in range(R):
        if g[j][i] != 0:
            res += g[j][i][2]
            g[j][i] = 0
            break
    g = MOVE()

print(res)