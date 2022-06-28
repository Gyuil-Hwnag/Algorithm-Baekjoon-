# 시간초과 때문에 Pypy3 으로 돌리기
import sys
input = sys.stdin.readline

n = int(input())
people = list(list(map(int, input().split())) for _ in range(n))
ch = [0]*n

mini = 10000001
def DFS(L, s):
    global mini
    if L==n//2:
        teamA, teamB = 0, 0
        for i in range(n):
            for j in range(n):
                if ch[i]==1 and ch[j]==1:
                    teamA+=people[i][j]
                elif ch[i]==0 and ch[j]==0:
                    teamB+=people[i][j]
        mini = min(mini, abs(teamA-teamB))
        return
    else:
        for i in range(s, n):
            if ch[i] == 0:
                ch[i]=1
                DFS(L+1, i+1)
                ch[i]=0
DFS(0, 0)
print(mini)