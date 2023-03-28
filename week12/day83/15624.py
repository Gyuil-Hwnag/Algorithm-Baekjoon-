## 15624
import sys
input = sys.stdin.readline

n = int(input())
res = [0, 1, 1]
for i in range(3, n+1):
    res.append((res[i-1] + res[i-2]) % 1000000007)

print(res[n])