import sys
input = sys.stdin.readline

N, L = map(int, input().split())
mid = 0
s = -1
res = 0
for i in range(L, 101):
    mid = (i*i-i) / 2
    if (N-mid)%i == 0 and (N-mid)//i >= 0:
        s = (N-mid) // i
        res = i
        break
if s == -1:
    print(-1)
else:
    for i in range(res):
        print(int(s+i), end=' ')