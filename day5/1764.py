import sys
input = sys.stdin.readline
n, m = map(int, input().split())

read = set()
see = set()

for i in range(n):
    read.add(input().strip())
for i in range(m):
    see.add(input().strip())

res = sorted(list(read & see))
print(len(res))
for i in res:
    print(i)