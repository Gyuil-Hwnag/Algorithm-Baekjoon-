## 7785
import sys
input = sys.stdin.readline

n = int(input())
people = dict()
for _ in range(n):
    name, state = map(str, input().split())
    if state == "enter":
        people[name] = state
    else:
        del people[name]

people = sorted(people.keys(), reverse=True)
for name in people:
    print(name)