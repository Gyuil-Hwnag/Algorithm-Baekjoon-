from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dQ = deque()

for i in range(n, 0, -1):
    dQ.append(i)

while len(dQ) > 1:
    res = dQ.pop()
    dQ.appendleft(dQ.pop())

print(dQ.pop())