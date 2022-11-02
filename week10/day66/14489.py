import sys
input = sys.stdin.readline

def SOLVE(A, B, C):
    if A+B>=2*C:
        print(A+B-2*C)
    else:
        print(A+B)

A, B = map(int, input().split())
C = int(input())
SOLVE(A, B, C)