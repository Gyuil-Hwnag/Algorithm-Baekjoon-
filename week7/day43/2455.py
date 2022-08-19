import sys
input = sys.stdin.readline
people = 0
max = 0
for _ in range(4):
    sub, add = map(int, input().split())
    people+=add
    people-=sub
    if people>max:
        max = people
print(max)