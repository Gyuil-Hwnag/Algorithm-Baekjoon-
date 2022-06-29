import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
dy = [0]*n
dy[0] = num[0]

res = max(num)
for i in range(1, n):
    if dy[i-1]+num[i]>0:
        dy[i] = dy[i-1]+num[i]
        if dy[i]>res:
            res = dy[i]

print(res)