## 2644
import sys
input = sys.stdin.readline

def dfs(L, num):
    global res
    num += 1
    visited[L] = True

    if L == target:
        res = num
        return
    
    for i in graph[L]:
        if not visited[i]:
            dfs(i, num)

n = int(input())
start, target = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
res = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(start, 0)
print(res-1)