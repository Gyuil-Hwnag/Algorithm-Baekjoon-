import sys
input = sys.stdin.readline

n = int(input())
line = list()
for _ in range(n):
    line.append(int(input()))
line.sort()
res = 0
for i in range(n):
    if line[i]*(n-i)>=max:
        res = line[i]*(n-i)
    # print(res)
print(res)