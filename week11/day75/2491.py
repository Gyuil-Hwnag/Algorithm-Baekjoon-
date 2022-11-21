import sys
input = sys.stdin.readline

def Solve():
    global n, num, dpDES, dpAES
    for i in range(1, n):
        if num[i]>=num[i-1]:
            dpAES[i] = max(dpAES[i-1]+1, dpAES[i])
        if num[i]<=num[i-1]:
            dpDES[i] = max(dpDES[i-1]+1, dpDES[i])
    
    print(max(max(dpAES), max(dpDES)))

n = int(input())
num = list(map(int, input().split()))
dpDES = list(1 for _ in range(n))
dpAES = list(1 for _ in range(n))
Solve()