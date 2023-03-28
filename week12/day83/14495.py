## 14495
import sys
input = sys.stdin.readline

n = int(input())
res = [1 for _ in range(117)]
for i in range(3, 117):
    res[i] = res[i-1] + res[i-3]

print(res[n-1]) 