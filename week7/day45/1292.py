import sys
input = sys.stdin.readline

n, m = map(int, input().split())
i = 1
num = list()
while len(num)<=m:
    for _ in range(i):
        num.append(i)
    i+=1
print(sum(num[n-1:m]))