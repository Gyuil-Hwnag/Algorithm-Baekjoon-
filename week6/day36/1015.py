import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
res = sorted(num)
result = list()
for i in range(n):
    idx = res.index(num[i])
    result.append(idx)
    res[idx] = -1

for i in result:
    print(i, end=' ')