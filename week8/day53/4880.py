import sys
input = sys.stdin.readline

def SOLVE(a, b, c):
    if c-b == b-a:
        print("AP " + str(c+c-b))
    elif b//a == c//b:
        print("GP " + str(int(c*(c/b))))

while True:
    a1, a2, a3 = map(int, input().split())
    if a1==0 and a2==0 and a3==0:
        break
    else:
        SOLVE(a1, a2, a3)