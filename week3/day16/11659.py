import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
res = list()

tmp = 0
res.append(0)
for i in num:
    tmp+=i
    res.append(tmp)

num = list()
for i in range(m):
    a, b = map(int, input().split())
    print(res[b]-res[a-1])