from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def BFS(x, y, weight, time, eat):
    q, can_eat = deque(), []
    q.append([x, y])
    c = [[-1]*n for _ in range(n)]
    c[x][y] = time
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx < n and 0 <= yy < n:
                    if c[xx][yy] == -1:
                        if a[xx][yy] == 0 or a[xx][yy] == weight:
                            c[xx][yy] = c[x][y] + 1
                            q.append([xx, yy])
                        elif 0 < a[xx][yy] < weight:
                            can_eat.append([xx, yy])
            qlen -= 1

        if can_eat:
            xx, yy = min(can_eat)
            eat += 1
            if eat == weight:
                eat = 0
                weight += 1
            a[xx][yy] = 0
            return xx, yy, weight, c[x][y] + 1, eat

    print(time)
    sys.exit()

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            x, y = i, j
            a[i][j] = 0

weight, time, eat = 2, 0, 0
while True:
    x, y, weight, time, eat = BFS(x, y, weight, time, eat)