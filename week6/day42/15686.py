import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
check = [0]*m

house=[]
chicken=[]
ch=[0]*m
res=21470000
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            house.append((i, j))
        elif board[i][j]==2:
            chicken.append((i, j))

# print(house)
# print(chicken)

def DFS(L, s):
    global res
    if L == m:
        sum = 0
        for j in range(len(house)):
            x1 = house[j][0]
            y1 = house[j][1]
            dis = 2147000
            for x in ch:
                x2=chicken[x][0]
                y2=chicken[x][1]
                dis=min(dis, abs(x1-x2)+abs(y1-y2))
            sum += dis
        if sum<res:
            res=sum
    else:
        for i in range(s, len(chicken)):
            ch[L]=i
            DFS(L+1, i+1)

DFS(0, 0)
print(res)