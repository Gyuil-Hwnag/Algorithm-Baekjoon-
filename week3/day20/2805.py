import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
lt = 1
rt = max(num)

while lt<=rt:
    mid = (lt+rt)//2
    res = 0
    for i in num:
        if i>mid:
            res+=(i-mid)
    if res>=m:
        lt = mid+1
    else:
        rt = mid-1

print(rt)