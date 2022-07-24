import sys
input = sys.stdin.readline
n = int(input())
work = list(list(map(int, input().split())) for _ in range(n))
dy = [0]*(n+1)
# print(work)
for i in range(n-1, -1, -1):
    if i+work[i][0] > n:
        dy[i] = dy[i+1]
    else:
        dy[i] = max(work[i][1]+dy[i+work[i][0]], dy[i+1])
        # print("%d %d" %(i, dy[i]))
print(dy[0])