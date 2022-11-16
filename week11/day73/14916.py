import sys
input = sys.stdin.readline

def Solve():
    global n
    dp = [-1, -1, 1, -1, 2, 1, 3, 2, 4, 3]
    for i in range(10,n+1):
        dp.append(dp[i-5]+1)
    return dp[n]

n = int(input())
print(Solve())