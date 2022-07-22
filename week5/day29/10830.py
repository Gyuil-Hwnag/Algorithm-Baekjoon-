import sys
input = sys.stdin.readline
n, b = map(int, input().split())
B = list(list(map(int, input().split())) for _ in range(n))

def MUL(n, A, B):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += A[i][k] * B[k][j]
                # print("N: %d K: %d M: %d res: %d" %(N, K, M, res[N][K]))
            res[i][j] %= 1000
    return res

def RECURSIVE(res, B):
    if B==1:
        return res
    if B==2:
        return MUL(n, res, res)
    else:
        temp = RECURSIVE(res, B//2)
        if B%2==0:
            return MUL(n, temp, temp)
        else:
            return MUL(n, MUL(n, temp, temp), res)

res = RECURSIVE(B, b)
for i in range(len(res)):
    for j in range(len(res[i])):
        print(res[i][j]%1000, end=' ')
    print()