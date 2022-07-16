import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

dy=[1]*n
first = min(num)
ch = list()
maxi = 0

for i in range(n):
    for j in range(i+1, n):
        if num[i]<num[j]:
            dy[j] = max(dy[j], dy[i]+1)

print(max(dy))