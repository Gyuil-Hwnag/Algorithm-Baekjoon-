import sys
input = sys.stdin.readline

s = int(input())
for _ in range(9):
    s -= int(input())
print(s)
