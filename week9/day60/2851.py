import sys
input = sys.stdin.readline

def SOLVE(req):
    for i in range(1, len(req)):
        req[i] = req[i-1]+req[i]
        if req[i]>=100:
            if req[i]-100 <= 100-req[i-1]:
                return req[i]
            else:
                return req[i-1]
    else:
        return req[-1]

num = []
for i in range(10):
    num.append(int(input()))

print(SOLVE(req = num))