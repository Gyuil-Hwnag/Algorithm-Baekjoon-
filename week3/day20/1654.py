import sys
input = sys.stdin.readline

N, K = map(int, input().split())
li = list(int(input()) for _ in range(N))
lt = 1
rt = max(li)

while lt<=rt:
    mid = (lt+rt)//2
    cnt = 0
    for i in li:
        cnt += i//mid
    
    if cnt>=K:
        lt = mid+1
    else:
        rt = mid-1

print(rt)