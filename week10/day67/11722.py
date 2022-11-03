import sys
input = sys.stdin.readline

def SOLVE():
    global n
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

n = int(input())
nums = list(map(int, input().split()))
print(SOLVE())