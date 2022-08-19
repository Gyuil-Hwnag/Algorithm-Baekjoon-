import sys
input = sys.stdin.readline

res = [0, 1, 3]
n = int(input())
for i in range(3, n+1):
  res.append(2*res[i-2]+res[i-1])
if n>3:
    print(res[-1] % 10007)
else:
    print(res[n])