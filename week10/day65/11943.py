import sys
input = sys.stdin.readline

def SOLVE(a, b, c, d):
    return min(a+d, b+c)

a, b = map(int, input().split())
c, d = map(int, input().split())

print(SOLVE(a, b, c, d))