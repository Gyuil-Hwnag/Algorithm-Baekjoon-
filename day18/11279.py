import sys
import heapq
input = sys.stdin.readline

hq = []
n = int(input())
for _ in range(n):
  num = int(input())
  if num == 0:
    if len(hq) == 0:
      print(0)
    else:
      print((-1)*heapq.heappop(hq))
  else:
    heapq.heappush(hq, (-1)*num)