import sys
input = sys.stdin.readline

n = int(input())
n1 = 1
n2 = 2

if n==1:
    print(1)
elif n==2:
    print(2)
else:
    for i in range(3, n+1):
        res = (n1+n2)%15746
        n1, n2 = n2, res
    print(res)

# 기존 Recursive Error
n = int(input())

def DFS(L):
    if L==1:
        return 1
    elif L==2:
        return 2
    else:
        return DFS(L-1)+DFS(L-2)

# 기존 메모리 초과
n = int(input())

dp = [0]*1000001
dp[1]=1
dp[2]=2
for i in range(3, n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n])