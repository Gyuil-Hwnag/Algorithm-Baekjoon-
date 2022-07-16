import sys
import heapq
input = sys.stdin.readline

n = int(input())
hq = list()
for i in range(n):
    s = int(input())
    if s==0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, (abs(s), s))