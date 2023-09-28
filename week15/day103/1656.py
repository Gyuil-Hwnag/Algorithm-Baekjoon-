## 1656
k,n = map(int,input().split())

lans = []
for _ in range(k):
    lans.append(int(input()))

left = 1
right = max(lans)
max_val = 0
while(left<=right):
    mid = (left+right)//2
    len_lans = 0
    for i in lans:
        len_lans += i//mid

    if(len_lans>=n):
        left = mid+1
        if(mid >max_val):
            max_val = mid
    else:
        right = mid-1

print(max_val)
print()