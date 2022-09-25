import gc
import sys
input = sys.stdin.readline

def GCD(a, b):
    res = 1
    for i in range(2, min(a, b)+1):
        if a%i==0 and b%i==0:
            res = max(res, i)
    return res

def LCM(gcd, a, b):
    return gcd*(a//gcd)*(b//gcd) 

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    gcd = GCD(a, b)
    lcm = (LCM(gcd, a, b))
    print(lcm, end=' ')
    print(gcd)