import sys
input = sys.stdin.readline

def Solve():
    global n, stay, dp
    for i in range(n):
        for j in range(1, stay[i]+1):
            if i+j<n:
                dp[i+j] = min(dp[i]+1, dp[i+j])
    
    # print(dp)
    if dp[n-1] >= sys.maxsize:
        print("-1")
    else:
        print(dp[n-1])


n = int(input())
stay = list(map(int, input().split()))
dp = list(sys.maxsize for _ in range(n))
dp[0] = 0
Solve()