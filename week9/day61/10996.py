import sys
input = sys.stdin.readline

def SOLVE(n):
    print('* '* (n-n//2))
    print(' *'* (n//2))

n = int(input())
for _ in range(n):
    SOLVE(n)