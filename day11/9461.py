import sys
input = sys.stdin.readline

dy = [0]*101
dy[0] = dy[1] = dy[2] = 1
dy[3] = dy[4] = 2

n = int(input())
for i in range(n):
    num = int(input())
    for i in range(5, num+1):
        if dy[i] == 0:
            dy[i] = dy[i-5]+dy[i-1]
    print(dy[num-1])