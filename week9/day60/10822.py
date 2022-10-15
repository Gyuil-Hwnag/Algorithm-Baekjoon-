import sys
input = sys.stdin.readline

def SOLVE(req):
    res = 0
    for i in req:
        res+=i
    return res

num = list(map(int, input().split(',')))
print(SOLVE(req = num))