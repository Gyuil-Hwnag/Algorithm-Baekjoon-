## 6131
import sys
input = sys.stdin.readline

def solve(n):
    res = 0
    for b in range(1, 501):
        for a in range(b, 501):
            if a**2 - b**2 == n:
                res+=1
    return res

n = int(input())
print(solve(n = n))