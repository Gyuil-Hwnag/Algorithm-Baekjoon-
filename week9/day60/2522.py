import sys
input = sys.stdin.readline

def SOLVE(n):
    for i in range(1, n+1):
        print(' '*(n-i)+"*"*i)
    for i in range(n-1, 0, -1):
        print(' '*(n-i)+"*"*i)

n = int(input())
SOLVE(n)