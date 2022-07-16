import sys
input = sys.stdin.readline

n, k = map(int, input().split())
res = 1

for i in range(n, n-k, -1):
    res *= i

for i in range(1, k+1):
    res = res//i

print(res)