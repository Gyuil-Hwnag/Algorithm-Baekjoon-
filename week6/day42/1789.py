from re import I
import sys
input = sys.stdin.readline

s = int(input().rstrip())
sum = 0
n = 0
while True:
    n += 1
    sum += n
    if sum > s:
        break

print(n-1)