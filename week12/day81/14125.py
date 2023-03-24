## 14125
import sys
input = sys.stdin.readline

def solve():
    global lines
    if sum(lines) - (2*max(lines)) > 0:
        return sum(lines)
    else:
        return 2 * (sum(lines)-max(lines)) - 1

lines = list(map(int, input().split()))
print(solve())