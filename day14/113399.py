import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
dy = [0]*n

num.sort()
wait = 0
res = list()
for i in range(n):
    wait += num[i]
    res.append(wait)

print(sum(res))