import sys
input = sys.stdin.readline

def SOLVE(req):
    s = [req[i] + req[i+4] for i in range(4)]
    res = max(s[0], 1) + max(s[1], 1)*5 + max(s[2], 0)*2 + s[3]*2
    print(res)

T = int(input())
for _ in range(T):
    li = list(map(int, input().split()))
    SOLVE(req = li)