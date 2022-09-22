import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

res = 0
for i in num:
    if i!= 0:
        if i%10 == n:
            res+=1
    else:
        if n==0:
            res+=1
print(res)