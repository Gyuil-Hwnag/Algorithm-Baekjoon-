import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = list(map(int, input().split()))
res = list()
res.append(sum(num[:k]))
for i in range(n-k):
    res.append(res[i]-num[i]+num[i+k])
print(max(res))