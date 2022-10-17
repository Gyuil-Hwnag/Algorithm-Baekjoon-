import sys
input = sys.stdin.readline

def SOLVE(req):
    for i in range(2, n+1):
        req[i] = req[i-1]+(i*5)-((i-1)*2)-1 
    return req[-1]%45678
    
n = int(input())

num = list(0 for _ in range(n+1))
num[0] = 0
num[1] = 5

print(SOLVE(req = num))