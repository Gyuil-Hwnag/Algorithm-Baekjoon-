import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
num.sort()
d1 = num[1]-num[0]
d2 = num[2]-num[1]
if d2 == d1:
    print(2*num[2]-d1)
elif d1 > d2:
    print(num[1]*2-num[2])
else:
    print(num[1]*2-num[0])