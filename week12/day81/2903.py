## 2903
import sys
input = sys.stdin.readline

def solve(L):
    global target
    target = 2*target-1
    if L > n:
        print(target*target)
    else:
        solve(L = L+1)

n = int(input())
target = 2
solve(target)