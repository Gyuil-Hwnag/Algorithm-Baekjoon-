import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
miro = list()
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
ch = []

for i in range(n):
    s = list(str(input().rstrip()))
    miro.append(s)

for y in range(n):
    for x in range(m):
        if miro[y][x] == 'R':
            miro[y][x] = '.'
            red = (y, x)
        elif miro[y][x] == 'B':
            miro[y][x] = '.'
            blue = (y, x)

dQ = deque()
dQ.append((red[0], red[1], blue[0], blue[1], 1))
ch.append((red[0], red[1], blue[0], blue[1]))

def move(y, x ,i):
    cnt = 1
    y+=dy[i]
    x+=dx[i]
    while miro[y][x] != '#' and miro[y][x] != 'O':
        x += dx[i]
        y += dy[i]
        cnt += 1
    return y-dy[i], x-dx[i], cnt-1

while dQ:
    # print(dQ)
    ry, rx, by, bx, cnt = dQ.popleft()
    if cnt>10:
        print(-1)
        exit(0)
    else:
        for i in range(4):
            rry, rrx, rc = move(ry, rx, i)
            bby, bbx, bc = move(by, bx, i)

            if miro[bby+dy[i]][bbx+dx[i]] != 'O':
                if miro[rry+dy[i]][rrx+dx[i]] == 'O':
                    print(cnt)
                    exit(0)

                if rrx==bbx and rry==bby:
                    if rc>bc:
                        rrx -= dx[i]
                        rry -= dy[i]
                    else:
                        bbx -= dx[i]
                        bby -= dy[i]

                if (rry, rrx, bby, bbx) not in ch:
                    ch.append((rry, rrx, bby, bbx))
                    dQ.append((rry, rrx, bby, bbx, cnt+1))
else:
    print(-1)