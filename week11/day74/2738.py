#2738
import sys
input = sys.stdin.readline

def Solve():
    global N, M
    A = list(list(map(int, input().split())) for _ in range(N))
    B = list(list(map(int, input().split())) for _ in range(N))
    for row in range(N):
        for col in range(M):
            print(A[row][col]+B[row][col], end=' ')
        print()

N, M = map(int, input().split())
Solve()