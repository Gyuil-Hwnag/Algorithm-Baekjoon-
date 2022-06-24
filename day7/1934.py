import sys
input = sys.stdin.readline

def lcm(a, b):
    if a<b:
        A, B = b, a
    else:
        A, B = a, b
    while b>0:
        a, b = b, a%b
    return A*B//a

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))