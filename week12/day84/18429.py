## 18429
import sys
input = sys.stdin.readline

def dfs(L, t):
    global cnt
    if L == N:
        cnt += 1
        return
    for i in range(N):
        if check[i] or t + kits[i] - K < 0:
            continue
        check[i] = 1
        dfs(L+1, t + kits[i] - K)
        check[i] = 0
        
N, K = map(int, input().split())
kits = list(map(int, input().split()))
check, cnt = [0]*N, 0
dfs(0, 0)
print(cnt)
