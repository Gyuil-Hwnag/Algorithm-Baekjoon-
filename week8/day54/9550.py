import sys
input = sys.stdin.readline

def SOLVE(candy, k):
    res = 0
    for i in candy:
        res += (i//k)
    return res

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    candy = list(map(int, input().split()))
    print(SOLVE(candy, k))
