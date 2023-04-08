## 18352
import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
  a, b =  map(int, input().split())  
  graph[a].append(b)

distance = [-1] *(N+1)
distance[X] = 0

def bfs():
   global graph
   dq = deque()
   dq.append(X)
   
   while dq:
    now = dq.popleft()
    for next in graph[now]:
        if distance[next] == -1:
           dq.append(next)
           distance[next] = distance[now]+1

bfs()
res = distance.count(K)
if res == 0:
   print(-1)
else:
    for i in range(len(distance)):
        if distance[i] == K:
            print(i)