## 9507
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    res = [1, 1, 2, 4]
    n = int(input())
    for i in range(4, n+1):
        res.append(res[i-1] + res[i-2] + res[i-3] + res[i-4])
    print(res[n])