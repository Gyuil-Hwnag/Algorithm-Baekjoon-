import sys
input = sys.stdin.readline

def SOLVE(array, n):
    dp = [1]*n
    dp[0] = array[0]  
    for i in range(1,n):
        for j in range(i):
            if array[j]<array[i]:
                dp[i]=max(dp[i], dp[j]+array[i])
            else:
                dp[i]=max(dp[i], array[i])

    return max(dp)

n=int(input())
array=list(map(int, input().split()))

print(SOLVE(array, n))