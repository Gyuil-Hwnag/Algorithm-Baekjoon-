import sys
input = sys.stdin.readline

def SOLVE(req):
    req.sort()
    if req[-2]-req[1] >= 4:
        return -1
    else:
        return sum(req)-req[-1]-req[0]

n = int(input())
for _ in range(n):
    num = list(map(int, input().split()))
    res = SOLVE(req=num)
    if res == -1:
        print("KIN")
    else:
        print(res)