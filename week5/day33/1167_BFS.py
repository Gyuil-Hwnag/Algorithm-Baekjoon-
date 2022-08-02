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

def BFS(start):
    queue = deque()
    queue.append([start, 0])

    visited = [0 for _ in range(v + 1)]
    maxd = 0
    maxi = start
    visited[start] = 1
    
    while queue:
        nowi, nowd = queue.popleft()
        if maxd < nowd:
            maxd = nowd
            maxi = nowi
        for e, d in dy[nowi]:
            if visited[e] == 0:
                queue.append([e, nowd + d])
                visited[e] = 1
    return maxi, maxd

tmpindex, tmpmax = BFS(1)
finalindex, finalmax = BFS(tmpindex)
print(finalmax)