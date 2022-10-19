import sys
from copy import deepcopy
input = sys.stdin.readline

n,q = map(int,input().split())
original_maps = [list(map(int,input().split())) for _ in range(0,2**n)]
magic_level = list(map(int,input().split()))

def DFS(x,y):
    global original_maps,n,visited,ans_sum

    stack=[(x,y)]
    area = 1
    visited[x][y]=1
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    ans_sum += original_maps[x][y]

    while(stack):
        cur_x,cur_y = stack.pop()
        for i in range(4):
            nx=cur_x+dx[i]
            ny=cur_y+dy[i]
            if (nx < 0 or nx >= 2 ** n or ny < 0 or ny >= 2 ** n):
                continue
            if(visited[nx][ny]==0 and original_maps[nx][ny]!=0):
                stack.append((nx,ny))
                visited[nx][ny]=1
                area+=1
                ans_sum+=original_maps[nx][ny]

    return area

def check_around():
    global original_maps,n

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    candidate =[]
    for i in range(2**n):
        for j in range(2**n):
            cnt=0
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if(nx<0 or nx>=2**n or ny<0 or ny>=2**n):
                    continue
                if(original_maps[nx][ny]!=0):
                    cnt+=1
            if(cnt<3 and original_maps[i][j]!=0):
                candidate.append((i,j))
    for location in candidate:
        x,y = location
        if(original_maps[x][y]>0):
            original_maps[x][y]-=1

for L in magic_level:
    variable_L = 2**L
    variable_N = 2**n
    copy_maps = [[0]*(2**n) for _ in range(2**n)]
    if(L==0):
        check_around()
        continue
    for i in range(0,2**n,2**L):
        for j in range(0,2**n,2**L):
            #시작점
            for l in range(0,2**L):
                for k in range(0,2**L):
                    #부분 격자 속 loop
                    copy_maps[i+k][j+((2**L) -1)-l] = original_maps[i+l][j+k]
    #격자 회전완료
    original_maps = deepcopy(copy_maps)
    check_around()
    #인접 조건 얼음감소 완료

visited = [[0]*(2**n) for _ in range(2**n)]
ans_sum =0
ans_area =-1

for i in range(2**n):
    for j in range(2**n):
        if(original_maps[i][j]!=0 and visited[i][j]==0):
            ans_area = max(ans_area, DFS(i,j))

print(ans_sum)
print(ans_area if ans_area!=-1 else 0)