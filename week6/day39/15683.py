import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
cctv = []
graph = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])

def FILL(board, mm, x, y):
    for i in mm:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7

def DFS(depth, arr):
    global mini

    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += arr[i].count(0)
        mini = min(mini, count)
        return
    
    temp = deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    
    for i in mode[cctv_num]:
        FILL(temp, i, x, y)
        DFS(depth+1, temp)
        temp = deepcopy(arr)


mini = n*m
DFS(0, graph)
print(mini)