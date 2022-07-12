import sys
import heapq
input = sys.stdin.readline

input = sys.stdin.readline

n = int(input())
lhq = []
rhq = []
res = list()

for _ in range(n):
    x = int(input())
    
    if len(lhq) == len(rhq):
        heapq.heappush(lhq, -x)
    
    else:
        heapq.heappush(rhq, x)
        
    if lhq and rhq and lhq[0] * -1 > rhq[0]:
        maxi = heapq.heappop(lhq)
        mini = heapq.heappop(rhq)
        
        heapq.heappush(lhq, mini * -1)
        heapq.heappush(rhq, maxi * -1)

    res.append(lhq[0] * -1)

for i in res:
    print(i)