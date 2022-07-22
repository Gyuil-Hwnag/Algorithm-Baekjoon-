import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(N))

M, K = map(int, input().split())
b = list(list(map(int, input().split())) for _ in range(M))

res = [[0]*K for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            res[n][k] += a[n][m] * b[m][k]
            # print("N: %d K: %d M: %d res: %d" %(N, K, M, res[N][K]))

for i in res:
    for j in i:
        print(j, end=' ')
    print()