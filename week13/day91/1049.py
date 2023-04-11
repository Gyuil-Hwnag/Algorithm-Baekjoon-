## 1049
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
prices = list()
for _ in range(M):
    prices.append(list(map(int, input().split())))

alls = sorted(prices, key=lambda x: x[0])
ones = sorted(prices, key=lambda x: x[1])
if N%6 == 0:
    res = min(alls[0][0]*(N//6), ones[0][1]*N)
else:
    if alls[0][0]*((N//6)+1) < ones[0][1]*N:
        res = alls[0][0]*((N//6)+1)
    elif alls[0][0]*(N//6) < ones[0][1]*N:
        res = alls[0][0]*(N//6) + ones[0][1]*(N%6)
    else:
        res = ones[0][1]*N
print(res)