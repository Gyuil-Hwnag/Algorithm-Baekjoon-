import sys
input = sys.stdin.readline

req = list(map(int, input().split(',')))
res = 0
for i in req:
    res+=i
print(res)