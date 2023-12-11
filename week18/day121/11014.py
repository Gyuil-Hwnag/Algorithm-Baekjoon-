## 11014
import sys
input = sys.stdin.readline

def bip_match(n, m):
    for nn, mm in [(n, m - 1), (n, m + 1), (n - 1, m - 1), (n - 1, m + 1), (n + 1, m - 1), (n + 1, m + 1)]:
        if 0 <= nn < N and 0 <= mm < M and not visited[nn][mm] and seat[nn][mm]:
            visited[nn][mm] = True
            if connect[nn][mm] == [-1, -1] or bip_match(connect[nn][mm][0], connect[nn][mm][1]):
                connect[nn][mm] = [n, m]       
                return True
    return False

for _ in range(int(input())):
    N, M = map(int, input().split())
    matrix = [input().strip() for _ in range(N)]
    
    seat = [[False] * M for _ in range(N)]
    answer = 0
    for n in range(N):
        for m in range(M):
            if matrix[n][m] == '.':
                seat[n][m] = True
                answer += 1
                
    connect = [[[-1] * 2 for _ in range(M)] for __ in range(N)]
    for n in range(N):
        for m in range(0, M, 2): 
            if seat[n][m]:
                visited = [[False] * M for _ in range(N)]
                if bip_match(n, m):
                    answer -= 1 
                    
    print(answer)