## 27433
import sys
input = sys.stdin.readline

def solve(L):
    global res
    if L == 0:
        return res
    res = res * L
    solve(L-1)

res = 1
n = int(input())
solve(n)
print(res)