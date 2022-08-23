import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n,l,r = map(int,input().split())
people = []

for _ in range(n):
    people.append(list(map(int,input().split())))

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

#국경선을 열지말지 결정하는 함수
def DFS(x, y, graph):
    ch[x][y]=True
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<n:
            if (not ch[xx][yy]) and (l<=(abs(graph[xx][yy] - graph[x][y]))<=r):
                loca.append((xx, yy))
                DFS(xx, yy, graph)
    #국경선을 연후 인구이동
    return loca

cnt = 0
while True:
    ch = [[False]*n for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(n):
            loca = [(i,j)]
            if not ch[i][j]:
                loca = DFS(i,j,people)            
            
            if len(loca)>1:
                flag = True
                sum = 0
                for x,y in loca:
                    sum+=people[x][y]
                avg = sum//len(loca)
                for a,b in loca:
                    people[a][b]=int(avg)

    if not flag:
        print(cnt)
        break
    cnt+=1