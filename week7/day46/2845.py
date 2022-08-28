import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
for i in num:
    print(i-(n*m), end=' ')