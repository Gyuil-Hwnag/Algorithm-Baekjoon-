import sys
input = sys.stdin.readline

n = int(input())
farm = list()
res = list()
for i in range(n):
    num = list(str(input().strip()))
    for j in range(len(num)):
        num[j] = int(num[j])
    farm.append(num)

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

cnt = 0
def DFS(x, y):
    global cnt
    if not 0<=x<n or not 0<=y<n:
        return False
    else:
        if farm[y][x]==1:
            cnt+=1
            farm[y][x]=0
            for i in range(4):
                DFS(x+dx[i], y+dy[i])
            return True

for i in range(n):
    for j in range(n):
        if DFS(i, j):
            res.append(cnt)
            cnt = 0

res.sort()
print(len(res))
for i in res:
    print(i)