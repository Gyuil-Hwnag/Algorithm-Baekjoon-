import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

dy = [0]*(n+1)

cnt = [0] * m
cnt[0] = 1
for i in range(1, n+1):
    dy[i] = dy[i-1]+num[i-1]
    cnt[dy[i]%m] += 1

res = 0
# nC2 에서 1을 두개 뽑을 경우 1-1 해서 나머지는 0, 0-0 에서 나머지는 0, 2-2는 나머지는 0
for i in cnt:
    res = res+((i*(i-1))//2)

# print(dy)
# print(cnt)
print(res)