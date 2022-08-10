import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
s = 0
for i in num:
    s+=(i**2)
print(s%10)