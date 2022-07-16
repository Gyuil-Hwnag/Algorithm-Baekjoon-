import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(list(map(int, input().split())) for _ in range(n))

dy = [[0]*(n+1) for _ in range(n+1)]

dy[1][1] = num[0][0]

for i in range(1, n+1):
    for j in range(1, n+1):
        dy[i][j] = dy[i-1][j]+dy[i][j-1]+num[i-1][j-1]-dy[i-1][j-1]

# r = list()
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if x1==x2 and y1==y2:
        res = num[x1-1][y1-1]
    else:
        res = dy[x2][y2] -(dy[x1-1][y2] + dy[x2][y1-1] - dy[x1-1][y1-1])
    print(res)
    # r.append(res)
# print(r)