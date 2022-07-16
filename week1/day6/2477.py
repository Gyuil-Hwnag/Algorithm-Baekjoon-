import sys
input = sys.stdin.readline
k = int(input())

h = 0
w = 0
wi = 0
hi = 0
slist = list()

for i in range(6):
    temp = list(map(int, input().split()))
    slist.append(temp)
    if temp[0] == 1 or temp[0] == 2:
        if w < temp[1]:
            w = temp[1]
            wi = i
    else:
        if h < temp[1]:
            h = temp[1]
            hi = i

s = [slist[hi - 1], slist[(hi + 1) % 6], slist[wi - 1], slist[(wi + 1) % 6]]

res = 1
for i in slist:
    if i not in s:
        res *= i[1]

print((w*h-res) * k)