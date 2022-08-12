import sys
input = sys.stdin.readline

a, b = 0, 1
n = int(input())
for i in range(n):
    a, b = a+b, a
print(a)