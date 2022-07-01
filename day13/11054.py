import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
re_num = num[::-1]
up = [1]*n
down = [1]*n
res = [0]*n

for i in range(n):
    for j in range(i):
        if num[i]>num[j]:
            up[i] = max(up[j]+1, up[i])
        if re_num[i]>re_num[j]:
            down[i] = max(down[j]+1, down[i])

for i in range(n):
    res[i] = up[i]+down[n-i-1]-1

print(max(res))