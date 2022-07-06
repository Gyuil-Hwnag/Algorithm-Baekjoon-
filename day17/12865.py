import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(list(map(int, input().split())) for _ in range(n))
li.sort(key= lambda x: (x[0]))
dy = [0]*(k+1)

for i in range(n):
    w, v = li[i][0], li[i][1]
    for j in range(k, w-1, -1):
        dy[j] = max(dy[j], dy[j-w] + v)

print(dy[-1])