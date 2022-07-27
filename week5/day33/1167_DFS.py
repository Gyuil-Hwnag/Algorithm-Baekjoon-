from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
dy = list([0]*(v+1))

for _ in range(v):
    s = list(map(int, input().split()))
    n = list()
    for i in range(1, len(s)-1, 2):
        start, price = s[i], s[i+1]
        n.append([start, price])
    dy[s[0]] = n

# for i in range(v+1):
#     print("i: %d, dy: %s" %(i, dy[i]))

def DFS(start, result):
    for e, d in dy[start]:
        if result[e] == 0:
            result[e] = result[start] + d
            DFS(e, result)

result1 = [0 for _ in range(v + 1)]
DFS(1, result1)  # 임의의 점 1에서 DFS 알고리즘을 이용하여 각 노드들까지의 거리 측정

result1[1] = 0
tmpmax = 0
tmpindex = 0
for i, x in enumerate(result1):
    if tmpmax < x:
        tmpmax = x
        tmpindex = i

result2 = [0 for _ in range(v + 1)]
DFS(tmpindex, result2)  # 첫번째 dfs 로 구해진 최대거리 노드에서 새로운 dfs 수행

result2[tmpindex] = 0
print(max(result2))