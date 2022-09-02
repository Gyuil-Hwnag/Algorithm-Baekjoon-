import sys
input = sys.stdin.readline

n = input().rstrip()
num = list()
for i in n:
    num.append(i)
num.sort(reverse=True)
res = ""
for i in num:
    res+=i

res = int(res)
if res%30==0:
    print(res)
else:
    print(-1)