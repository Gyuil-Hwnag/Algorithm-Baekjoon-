import sys
input = sys.stdin.readline

def FINGER(n):
    if n==0:
        print(2)
    elif 0<n<=5:
        print(n)
    else:
        print(10-n)

n = int(input())
FINGER(n%8)