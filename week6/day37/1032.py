import sys
input = sys.stdin.readline

n = int(input())
order = list()
for i in range(n):
    order.append(list(input().rstrip()))
# print(order)

for i in range(len(order[0])):
    ch = True
    for j in range(1, n):
        if order[0][i] != order[j][i]:
            ch = False
            break
    if not ch:
        order[0][i] = '?'

for i in order[0]:
    print(i, end='')