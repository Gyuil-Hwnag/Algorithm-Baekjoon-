import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]

def UP(board):
    for i in range(n):
        top = 0
        x = 0
        for j in range(n):
            if board[j][i] == 0:
                continue
            if x==0:
                x = board[j][i]
            else:
                if x==board[j][i]:
                    board[top][i] = x*2
                    x=0
                    top+=1
                else:
                    board[top][i] = x
                    x = board[j][i]
                    top+=1
            board[j][i]=0
        if x!=0:
            board[top][i] = x
    return board

def DOWN(board):
    for i in range(n):
        top = n-1
        x = 0
        for j in range(n-1, -1, -1):
            if board[j][i]==0:
                continue
            if x==0:
                x = board[j][i]
            else:
                if x==board[j][i]:
                    board[top][i] = x*2
                    x = 0
                    top-=1
                else:
                    board[top][i] = x
                    x = board[j][i]
                    top-=1
            board[j][i]=0
        if x!=0:
            board[top][i] = x
    return board

def LEFT(board):
    for i in range(n):
        top = 0
        x = 0
        for j in range(n):
            if board[i][j]==0:
                continue
            if x==0:
                board[i][j]
            else:
                if x==board[i][j]:
                    board[i][top] = x*2
                    x=0
                    top+=1
                else:
                    board[i][top] = x
                    x = board[i][j]
                    top+=1
            board[i][j] = 0
        if x != 0:
            board[i][top] = x
    return board

def RIGHT(board):
    for i in range(n):
        top = n-1
        x = 0
        for j in range(n-1, -1, -1):
            if board[i][j]==0:
                continue
            if x==0:
                board[i][j]
            else:
                if x==board[i][j]:
                    board[i][top] = x*2
                    x=0
                    top-=1
                else:
                    board[i][top] = x
                    x = board[i][j]
                    top-=1
            board[i][j] = 0
        if x != 0:
            board[i][top] = x
    return board 

res = 0
def DFS(board, cnt):
    global res
    if cnt==4:
        for i in range(n):
            for j in range(n):
                res = max(res, board[i][j])
        return

    DFS(UP(deepcopy(board)), cnt+1)
    DFS(DOWN(deepcopy(board)), cnt+1)
    DFS(LEFT(deepcopy(board)), cnt+1)
    DFS(RIGHT(deepcopy(board)), cnt+1)

DFS(num, 0)
print(res)