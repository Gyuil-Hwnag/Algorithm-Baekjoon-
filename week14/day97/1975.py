## 1975
import sys
input = sys.stdin.readline

def NumberGame(n, i):
    return 1 + NumberGame(n//i, i) if n%i == 0 else 0

for _ in range(int(input())):
    N = int(input())
    cnt = 0
    for i in range(2, N+1):
        cnt += NumberGame(N, i)
    print(cnt)