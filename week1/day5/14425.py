import sys
n, m = map(int, sys.stdin.readline().split())
s = set(sys.stdin.readline() for _ in range(n))
ch = 0

for _ in range(m):
    c = sys.stdin.readline()
    if c in s:
        ch += 1

print(ch)