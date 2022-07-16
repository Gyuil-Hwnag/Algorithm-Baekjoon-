import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dy = [0]*(n+1)

def DFS(L):
    if L == n+1:
        if sum(dy) == m:
            res = ""
            for i in range(len(dy)):
                if dy[i]!=0:
                    res = res+str(i)+" "
            print(res)
            return
        else:
            return
    else:
        if sum(dy) == m:
            res = ""
            for i in range(len(dy)):
                if dy[i]!=0:
                    res = res+str(i)+" "
            print(res)
            return
        else:
            dy[L] = 1
            DFS(L+1)
            dy[L] = 0
            DFS(L+1)
DFS(1)