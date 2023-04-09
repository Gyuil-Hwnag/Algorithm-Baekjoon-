## 16953
import sys
input = sys.stdin.readline

def dfs(L, num):
    global res, target
    if num > target:
        return 
    elif num == target:
        if L < res:
            res = L
    else:
        dfs(L = L+1, num = num*2)
        dfs(L = L+1, num = num*10+1)

res = 10**9
start, target = map(int, input().split())
dfs(L = 1, num = start)

if res == 10**9:
    print(-1)
else:
    print(res)