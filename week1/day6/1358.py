from math import hypot
import sys
input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())
r = h/2
cnt = 0
for i in range(p):
    hx, hy = map(int, input().split())
    if (x <= hx <= x+w) and (y <= hy <= y+h):
        cnt +=1
        continue
    r = h/2
    d1 = ((hx-x)**2 + (hy-(y+r))**2)**0.5
    d2 = ((hx-(x+w))**2 + (hy-(y+r))**2)**0.5
    if d1 <= r or d2 <= r:
        cnt += 1
print(cnt)