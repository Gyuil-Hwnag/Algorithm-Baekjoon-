import sys
input = sys.stdin.readline

n, m = map(int, input().split())
miro = list()

def INPUT():
    global n
    global miro
    for _ in range(n):
        miro.append(list(map(int, input().split())))

def SOLVE():
    global n, m
    dp = list(list(0 for _ in range(m)) for _ in range(n))
    dp[0][0] = miro[0][0]
    for i in range(1, m):
        dp[0][i] = miro[0][i]+dp[0][i-1]
    for i in range(1, n):
        dp[i][0] = miro[i][0]+dp[i-1][0]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = miro[i][j]+max(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
    return dp[-1][-1]

INPUT()
print(SOLVE())