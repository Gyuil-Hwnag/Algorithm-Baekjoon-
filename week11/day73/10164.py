import sys
input = sys.stdin.readline

def Solve():
    global N, M, K
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    dp[0][1], step = 1, 1
    sy, sx = 0, 0

    for i in range(1, N+1):
        for j in range(1, M+1):
            if step == K:
                sy, sx = i, j
            step += 1
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    answer = dp[sy][sx] * dp[N-sy+1][M-sx+1] if K else dp[N][M]
    return answer

N, M, K = map(int, input().split())
print(Solve())