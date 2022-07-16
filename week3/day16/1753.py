import sys
input = sys.stdin.readline
import heapq

v, e = map(int, input().split())
k = int(input())
node = list([] for _ in range(v+1))

for i in range(e):
    u, v, w = map(int ,input().split())
    node[u].append((v, w))

distance = [100000000]*(v+1)

q = []
def dijkstra(start):
    distance[start] = 0 
    heapq.heappush(q, (0,start))
    while q:
        # print("q: %s" %(q))
        # print("node: %s" %(node))
        # print("distance: %s" %(distance))
        dist, now_node = heapq.heappop(q)
        for n_n, weight in node[now_node]:
            cost = dist + weight
            if cost < distance[n_n]:
                distance[n_n] = cost
                heapq.heappush(q,(cost,n_n))

dijkstra(k)
for i in distance[1:]:
    if i != 100000000:
        print(i)
    else:
        print("INF")