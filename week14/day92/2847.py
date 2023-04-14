## 2847
import sys
input = sys.stdin.readline

N = int(input())
levels = list()
for _ in range(N):
    levels.append(int(input().rstrip()))

res = 0
for i in range(N-2, -1, -1):
    while levels[i] >= levels[i+1]:
        res += 1
        levels[i] -= 1
print(res)