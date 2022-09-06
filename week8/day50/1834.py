import sys
input = sys.stdin.readline

n = int(input())
res = 0
for i in range(n+1, n*n, n+1):
    if i//n == i%n:
        res+=i
print(res)