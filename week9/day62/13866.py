import sys
input = sys.stdin.readline

def SOLVE(req):
    req.sort()
    return abs(req[-1]-req[-2]+req[0]-req[1])

num = list(map(int, input().split()))
print(SOLVE(req=num))