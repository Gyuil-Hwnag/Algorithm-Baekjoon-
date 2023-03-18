import sys
input = sys.stdin.readline

def gcd(x, y):
    mod = x%y
    while mod>0:
        x = y
        y = mod
        mod = x%y
    return y

a, b = map(int, input().split())
c, d = map(int, input().split())
resA = a*d + b*c
resB = b*d
n = gcd(resA, resB)
print(resA//n, resB//n)