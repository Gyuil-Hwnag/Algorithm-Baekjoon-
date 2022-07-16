import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
p = list(map(int, input().split()))

cost = p[0]
res = l[0]*p[0]
for i in range(1, n-1):
    if p[i]<cost:
        cost=p[i]
    res = res+(l[i]*cost)
print(res)