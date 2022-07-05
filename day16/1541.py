import sys
input = sys.stdin.readline

x = list(map(str, input().rstrip().split('-')))
n = list()

for i in x:
    s = i.split('+')
    num = 0
    for j in s:
        num+=int(j)
    n.append(num)

res = n[0]

for i in range(1, len(n)):
    res-=n[i]
print(res)