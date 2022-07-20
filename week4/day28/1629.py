import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
def RECURSIVE(a, b):
    if b==1:
        return a%c
    
    tmp = RECURSIVE(a, b//2)
    if b%2==0:
        return tmp*tmp%c
    else:
        return tmp*tmp*a%c

print(RECURSIVE(a, b))