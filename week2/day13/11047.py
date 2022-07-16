import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = list(int(input()) for _ in range(n))

res = 0
for i in range(n-1, -1, -1):
    if coin[i] <= k:
        res = res+(k//coin[i])
        k = k%coin[i]
    if k==0:
        break
print(res)