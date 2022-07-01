import sys
input = sys.stdin.readline

n = int(input())
room = list(list(map(int, input().split())) for _ in range(n))
room.sort(key = lambda x : (x[1], x[0]))

tmp = 0
cnt = 0
for s, e in room:
    if s >= tmp:
        cnt += 1
        tmp = e
print(cnt)