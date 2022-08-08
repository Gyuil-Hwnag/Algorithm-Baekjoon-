import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
num.sort()

res = min(num)
while True:
    cnt = 0
    for i in range(5):
        if res%num[i] == 0:
            cnt+=1
    if cnt >= 3:
        break
    res+=1

print(res)