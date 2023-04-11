## 16435
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
apples = list(map(int, input().split()))
apples.sort()

for apple in apples:
    if L >= apple:
        L += 1
print(L)