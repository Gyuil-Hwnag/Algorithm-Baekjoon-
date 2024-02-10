## 7770
import sys

input = sys.stdin.readline
n = int(input())
i = 1
res = 0
while True:
    res += i**2 + (i-1)**2
    if res > n:
        print(i-1)
        break
    i += 1