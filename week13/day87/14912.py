## 14912
import sys
input = sys.stdin.readline

def solve():
    global n, t, res
    target = str(t)
    for i in range(1, n+1, 1):
        s = str(i)
        res += s.count(target)
    return res

n, t = map(int, input().split())
res = 0
print(solve())