## 200006
import sys
input = sys.stdin.readline

p, m = map(int, input().split())
people = []
for _ in range(p):
    level, id = input().split()
    people.append([int(level), id])

rooms = []

for level, id in people:
    state = False
    for i in range(len(rooms)):
        if len(rooms[i][1]) == m: continue
        if rooms[i][0] - 10 <= level <= rooms[i][0] + 10:
            state = True
            rooms[i][1].append([level, id])
            break

    if not state:
        rooms.append([level, [[level, id]]])

for i in range(len(rooms)):
    if len(rooms[i][1]) == m:
        print('Started!')
        ids = sorted(rooms[i][1], key=lambda x: x[1])
        for j in range(m):
            print(*ids[j])
    else:
        print('Waiting!')
        ids = sorted(rooms[i][1], key=lambda x: x[1])
        for j in range(len(ids)):
            print(*ids[j])
