import sys
input = sys.stdin.readline

n = int(input())
city = list(list(map(int, input().split())) for _ in range(n))
res = sys.maxsize
visited = [False for _ in range(n)]

def dfs(start, pay, point, L):
    global res
    if L==n:
        if city[point][start] != 0:
            res = min(pay+city[point][start], res)
        return
    else:
        for i in range(n):
            if visited[i] == False and city[point][i] != 0:
                visited[i] = True
                dfs(start=start, pay = pay+city[point][i], point=i, L = L+1)
                visited[i] = False

for i in range(n):
    visited[i] = True
    dfs(start=i, pay=0, point=i, L=1)
    visited[i] = False

print(res)