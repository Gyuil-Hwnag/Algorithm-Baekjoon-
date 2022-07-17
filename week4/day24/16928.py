import sys
from collections import deque
input = sys.stdin.readline

dy = [False]*101
res = [0]*101
n, m = map(int, input().split())
ladder = {}
for _ in range(n):
    s, e = map(int, input().split())
    ladder[s] = e

snake = {}
for _ in range(m):
    s, e = map(int, input().split())
    snake[s] = e

dQ = deque()
dQ.append((1))
dy[1] = True

while dQ:
    x = dQ.popleft()
    if x==100:
        print(res[100])
        exit(0)
    else:
        for i in range(1, 7):
            xx = x+i
            if xx in ladder.keys():
                xx = ladder[xx]
            if xx in snake.keys():
                xx = snake[xx]
            if xx<=100 and dy[xx] == False:
                dy[xx] = True
                res[xx] = res[x]+1
                dQ.append(xx)