import sys
input = sys.stdin.readline

n = int(input())
li = list(list(map(int, input().split())) for _ in range(n))
li.sort(key = lambda x: (x[0]))

dy = [1]*(n)
maxi = 0
for i in range(n):
    ch = li[i][1]
    for j in range(i):
        if li[j][1] < ch:
            dy[i] = max(dy[i], dy[j]+1)

print(n-max(dy))