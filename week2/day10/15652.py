import sys
input = sys.stdin.readline

n,k = map(int, input().split())
 
s = list()
def DFS(start):
    if len(s)== k:
        res = ""
        for i in s:
            res = res+str(i)+" "
        print(res)
        return
    
    for i in range(start, n+1):
        s.append(i)
        DFS(i)
        s.pop()

DFS(1)