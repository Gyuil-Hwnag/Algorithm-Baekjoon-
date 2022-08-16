import sys
input = sys.stdin.readline

# 가지치기 & 4보다 커지면 바로 리턴
def DFS(L, num):
    global res
    if L>=res:
        return
    
    if check():
        res = L
        return
    
    for idx in range(num+1, len(board)):
        i, j = board[idx]
        if lines[i][j-1] == 0 and lines[i][j+1] == 0:
            lines[i][j] = 1
            DFS(L+1, idx)
            lines[i][j] = 0
            
def check():
    for i in range(1, n+1):
        now = i
        for j in range(1, h+1):
            if lines[j][now] == 1:
                now += 1
            elif lines[j][now-1] == 1:
                now -= 1
        if i != now:
            return False
    return True

n, m, h = map(int, input().split())
lines = [[0 for _ in range(n+1)] for _ in range(h+1)]
board = []
res = 4

# 라인 연결해주기
for _ in range(m):
    a, b = map(int, input().split())
    lines[a][b] = 1

# 앞뒤로 연결된 것이 없을 경우들 넣어두기
for i in range(1, h+1):
    for j in range(1, n):
        if lines[i][j]==0 and lines[i][j-1]==0 and lines[i][j+1]==0:
            board.append([i, j])

DFS(0, -1)
if res<4:
    print(res)
else:
    print(-1)