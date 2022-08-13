import sys
input = sys.stdin.readline

n, result = map(int, input().split())
num = list(map(int, input().split()))

cnt = 0
def DFS(L, sum):
    global cnt
    if L>=n:
        return
    if sum+num[L]==result:
        cnt+=1
    DFS(L+1, sum+num[L])
    DFS(L+1, sum)
            
DFS(0, 0)
print(cnt)    