import sys
input = sys.stdin.readline

s = int(input())
n = int(input())
for i in range(n):
    p, num = map(int, input().split())
    s -= (p*num)
if s == 0:
    print("Yes")
else:
    print("No")