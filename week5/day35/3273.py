import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort()
t = int(input())

cnt = 0
s = 0
e = n-1
while s<e:
    res = num[s]+num[e]
    if res>t:
        e-=1
    elif res==t:
        s+=1
        e-=1
        cnt+=1
    else:
        s+=1

print(cnt)