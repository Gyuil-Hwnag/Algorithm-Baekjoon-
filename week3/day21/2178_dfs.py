import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
miro = list()
res = 0
for i in range(n):
    num = list(str(input()))
    for j in range(m):
        num[j] = int(num[j])
        if num[j] == 1:
            res+=1
    miro.append(num)

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def DFS(x, y, cnt):
    global res
    if cnt>res:
        return
    if x==m-1 and y==n-1:
        if cnt<res:
            res = cnt
        return
    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<m and 0<=yy<n:
                if miro[yy][xx]==1:
                    miro[yy][xx]=0
                    DFS(xx, yy, cnt+1)
                    miro[yy][xx]=1
DFS(0, 0, 1)
print(res)