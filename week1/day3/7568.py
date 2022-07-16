n = int(input())
people = list()
res = [1]*n

for i in range(n):
    w, h = map(int, input().split())
    people.append([w, h])

for i in range(n):
    for j in range(n):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                res[i] += 1

for i in res:
    print(i, end=' ')