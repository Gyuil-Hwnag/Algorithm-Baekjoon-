import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
target = int(input())
res = 0

for i in num:
    if i == target:
        res+=1
print(res)