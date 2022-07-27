import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dy = [0]*(n+1)
arr = []
def DFS(s):
    for i in graph[s]:
        if dy[i] == 0:
            dy[i] = s
            DFS(i)

DFS(1)
for i in range(2, n+1):
    print(dy[i])

# print(dy)

# for i in graph:
#     print(i)