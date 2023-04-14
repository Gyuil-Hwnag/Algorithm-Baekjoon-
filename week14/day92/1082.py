## 1082
import sys
input = sys.stdin.readline

def flip(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            A[x][y] = 1 - A[x][y]

def solve():
    global A, B, N, M, res
    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                flip(i, j)
                res += 1

            if A == B:
                return
        if A == B:
            return

N, M = map(int, input().split())
A = list()
B = list()

for _ in range(N):
    A.append(list(map(int, input().rstrip())))
for _ in range(N):
    B.append(list(map(int, input().rstrip())))

res = 0
solve()

if A != B:
    print(-1)
else:
    print(res)