import sys
input = sys.stdin.readline

a, b = map(int, input().split())
def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

def lcm(a, b, c):
    return a*b//c

c = gcd(a, b)
print(c)
print(lcm(a, b, c))