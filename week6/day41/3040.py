import sys
input = sys.stdin.readline

people = list(int(input().rstrip()) for _ in range(9))
check = False
res = list()

for i in range(8):
    if not check:
        for j in range(i+1, 9):
            if (sum(people)-people[i]-people[j])==100:
                res.append(i)
                res.append(j)
                check = True
    else:
        break

for i in range(9):
    if i not in res:
        print(people[i])