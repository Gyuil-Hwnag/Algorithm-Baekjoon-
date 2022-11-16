import sys
input = sys.stdin.readline

def Solve():
    global dp, n
    for i in range(3, n+1):
        dp.append(dp[i-1]+dp[i-2])
    print(dp[n])

n = int(input())
dp = [0, 1, 1]
Solve()