import sys
input = sys.stdin.readline

def SUMGCD(n):
    res = 0
    for i in range(1, n+1):
        res += (n//i)*i
    return res

N = int(input())
print(SUMGCD(N))