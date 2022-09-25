import sys
input = sys.stdin.readline

def SOLVE(req):
    res = 0
    for i in req:
        if i == 0:
            res+=1
    res = (4+res)%5
    return chr(res+65)

for _ in range(3):
    yut = list(map(int, input().split()))
    res = SOLVE(yut)
    print(res)