import sys
input = sys.stdin.readline

def Solve():
    global box, n
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if box[i] > box[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

n = int(input())
box = list(map(int, input().split()))
print(Solve())