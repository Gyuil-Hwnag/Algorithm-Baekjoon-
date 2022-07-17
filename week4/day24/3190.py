import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
k = int(input())
apple = list([0]*n for _ in range(n))

for i in range(k):
    y, x = map(int, input().split())
    apple[y-1][x-1] = 1

num = int(input())
times = {}
for i in range(num):
    x, c = input().split()
    times[int(x)] = c


# 상, 좌, 하, 우
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
def MOVE(i, M):
    if M == 'D':
        if i==0:
            i = 3
        else:
            i = i-1
    else:
        i = (i+1)%4
    return i

d = 3
y, x = 0, 0
dQ = deque()
dQ.append([y, x])
apple[y][x] = 2
time = 1

while dQ:
    # print(time)
    # print(dQ)
    # for i in apple:
    #     print(i)

    y, x = y+dy[d], x+dx[d]
    # print("%d %d %d" %(x, y, d))
    if 0<=y<n and 0<=x<n and apple[y][x] != 2:
        if apple[y][x] == 0:
            yy, xx = dQ.popleft()
            apple[yy][xx] = 0
        
        apple[y][x] = 2
        dQ.append([y, x])

        if time in times.keys():
            d = MOVE(d, times[time])
        time+=1
    else:
        print(time)
        exit(0)