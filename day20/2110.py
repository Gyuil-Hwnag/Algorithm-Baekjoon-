import sys
input = sys.stdin.readline

n, c = map(int, input().split())
home = list(int(input()) for _ in range(n))
home.sort()

lt = 1
rt = home[-1]-home[0]
res = 0

while lt<=rt:
    mid = (lt+rt)//2
    cnt = 1
    point = home[0]
    for i in range(1, n):
        if home[i] >= point+mid:
            cnt+=1
            point = home[i]
    
    if cnt >= c:
        lt = mid+1
        res = max(res, mid)
    else:
        rt = mid-1

print(res)