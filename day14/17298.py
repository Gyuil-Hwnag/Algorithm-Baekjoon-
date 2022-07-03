from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
stack = deque()
num = list(map(int, input().split()))
dy = [-1]*n

for i in range(n):
    while stack and num[stack[-1]] < num[i]:
        dy[stack.pop()] = num[i]
    stack.append(i)

for i in dy:
    print(i, end=' ')