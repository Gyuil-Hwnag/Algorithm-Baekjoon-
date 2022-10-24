import sys
input = sys.stdin.readline

def SOLVE(n, m):
    if m<=2:
        print("NEWBIE!")
    elif 2<m<=n:
        print("OLDBIE!")
    else:
        print("TLE!")

n, m = map(int, input().split())
SOLVE(n, m)