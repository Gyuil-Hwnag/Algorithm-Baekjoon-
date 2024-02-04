## 23813
import sys
input = sys.stdin.readline

n = list(input())
total = 0
for i in range(len(n)):
    n.insert(0, n[-1])
    del n[-1]
    total += int("".join(n))
print(total)