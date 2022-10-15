import sys
input = sys.stdin.readline

n = int(input())

num = list(0 for _ in range(n+1))
num[0] = 0
num[1] = 5

for i in range(2, n+1):
    num[i] = num[i-1]+(i*5)-((i-1)*2)-1

print(num[n]%45678)