import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
# cnt = 0
cnt = n
# print(a)
for i in range(len(a)):
    # if a[i]>=0:
    #     cnt+=1
    #     a[i] = a[i]-b
    a[i] = a[i]-b
    if a[i] > 0:
        if a[i]%c == 0:
            cnt = cnt+(a[i]//c)
        else:
            cnt = cnt+((a[i]//c)+1)
        a[i] = 0
    # print(cnt)
print(cnt) 