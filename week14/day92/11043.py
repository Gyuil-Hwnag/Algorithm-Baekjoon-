## 11403
import sys
from collections import deque
input = sys.stdin.readline

def solve():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                    graph[i][j] = 1

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

solve()
for row in graph:
    for col in row:
        print(col, end= " ")
    print()