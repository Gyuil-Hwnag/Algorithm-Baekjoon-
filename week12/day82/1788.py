## 1788
import sys
input = sys.stdin.readline

def solve():
    global n, res
    for i in range(2, abs(n) + 1):
        res.append((res[i - 1] + res[i - 2]) % 1000000000)

def resPrint():
    global n, res
    if n % 2 == 0 and n < 0:
        print(-1)
    elif n == 0:
        print(0)
    else:
        print(1)
    print(res[abs(n)])

n = int(input())
res = [0, 1]

solve()
resPrint()