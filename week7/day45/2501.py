import sys
input = sys.stdin.readline

n, k = map(int, input().split())
res = list()
for i in range(1, n+1):
    if n%i==0:
        res.append(i)
# print(res)
if len(res)>=k:
    print(res[k-1])
else:
    print(0)