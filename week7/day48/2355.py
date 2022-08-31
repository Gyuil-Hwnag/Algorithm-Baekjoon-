import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a, b = max(a, b), min(a, b)
n = a-b
s = ((n*(n+1))//2+(n+1)*b)
print(s)