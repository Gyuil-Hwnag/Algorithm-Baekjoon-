import sys
input = sys.stdin.readline

dy = [0]*11
dy[1] = 1
dy[2] = 2
dy[3] = 4

for i in range(4, 11):
    dy[i] = sum(dy[i-3:i])

T = int(input())
for _ in range(T):
    print(dy[int(input())])