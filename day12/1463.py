import sys
input = sys.stdin.readline

n = int(input())
# 방법1 
dp = [0] * (n+1)
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
        
print(dp[n])

# 방법2 효율 안좋은 방법 거의 2배 차이남(메모리, 속도)
dy = [10**6]*(3*(10**6))
dy[0] = 0
dy[1] = 0
dy[2] = 1
dy[3] = 1

for i in range(1, n):
    dy[i*3] = min(dy[i]+1, dy[i*3])
    dy[i*2] = min(dy[i]+1, dy[i*2])
    dy[i+1] = min(dy[i]+1, dy[i+1])

print(dy[n])