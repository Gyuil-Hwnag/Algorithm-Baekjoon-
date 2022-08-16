import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n) :
    y, x, d, g = map(int, input().split())
    graph[x][y] = 1

    # 커브 리스트
    curve = [d]
    for j in range(g):
        for k in range(len(curve)-1, -1, -1):
            curve.append((curve[k]+1)%4)
    # print(curve)

    # 드래곤 커브
    for j in range(len(curve)):
        x += dx[curve[j]]
        y += dy[curve[j]]
        if not 0<=x<101 or not 0<=y<101:
            continue
        graph[x][y] = 1
        # for i in graph:
        #     print(i)

res = 0
for i in range(100):
    for j in range(100):
        if graph[i][j]==1 and graph[i+1][j]==1 and graph[i][j+1]==1 and graph[i+1][j+1]==1:
            res += 1

print(res)
