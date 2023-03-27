## 13301
import sys
input = sys.stdin.readline

def dp(L):
    global res
    if L == n:
        return 
    else:
        num = res[L-1]+res[L-2]
        res.append(num)
        dp(L+1)

n = int(input())
res = [4, 6, 10]
if n > 3:
    dp(3)
    print(res[-1])
else:
    print(res[n-1])
