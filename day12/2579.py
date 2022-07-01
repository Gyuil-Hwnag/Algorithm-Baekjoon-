import sys
input = sys.stdin.readline

n = int(input())
num = list(int(input()) for _ in range(n))
dy = [0]*(n)
if n >= 3:
    dy[0] = num[0]
    dy[1] = num[0]+num[1]
    dy[2] = max(num[1] + num[2], num[0] + num[2])

    for i in range(3, n):
        dy[i] = max(dy[i-3]+num[i-1]+num[i], dy[i-2]+num[i])
    print(dy[n-1])
else:
    if n == 1:
        print(num[0])
    elif n==2:
        print(num[0]+num[1])
    else:
        print(0)