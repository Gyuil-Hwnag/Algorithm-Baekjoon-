import sys
input = sys.stdin.readline

def dfs(N, M, num):
    s, e = 0, 0
    sum = num[0]
    cnt = 0
    while True:
        if sum < M:
            e += 1
            if e >= N:
                break
            sum += num[e]
        elif sum == M:
            cnt += 1
            sum -= num[s]
            s += 1
        else:
            sum -= num[s]
            s += 1
    return cnt

N, M = map(int, input().split())
num = list(map(int, input().split()))
print(dfs(N, M, num))