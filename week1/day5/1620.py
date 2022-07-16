import sys
n, m = map(int, sys.stdin.readline().split())
my = dict()
for i in range(n):
    s = sys.stdin.readline().rstrip()
    my[str(i+1)] = s
    my[s] = i+1

for _ in range(m):
    s = sys.stdin.readline().rstrip()
    print(my[s])
