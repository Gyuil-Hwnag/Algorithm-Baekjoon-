import sys
input = sys.stdin.readline

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

n = int(input())
num = list(map(int, input().split()))
target = num[0]
for i in range(1, n):
    g = gcd(target, num[i])
    print("%d/%d" %(target//g, num[i]//g))