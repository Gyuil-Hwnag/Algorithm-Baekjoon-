import sys
input = sys.stdin.readline

n = int(input())
num = list(list(map(int, input().split())) for _ in range(n))

for i in range(n-2, -1, -1):
    for j in range(len(num[i])):
        num[i][j] = max(num[i+1][j], num[i+1][j+1])+num[i][j]

print(num[0][0])
