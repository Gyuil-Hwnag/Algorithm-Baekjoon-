import sys
input = sys.stdin.readline

a, i = map(int, input().split())

if a>0 and i>0:
    print(a*(i-1)+1)