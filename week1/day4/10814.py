import sys
n = int(sys.stdin.readline())
p = list()
for i in range(n):
    p.append(sys.stdin.readline().split())

p.sort(key = lambda x: int(x[0]))

for i in p:
    print(i[0], i[1])