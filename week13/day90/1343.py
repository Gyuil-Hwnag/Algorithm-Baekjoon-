## 1343
import sys
input = sys.stdin.readline

target = input().strip()

def solve():
    global target
    target = target.replace("XXXX", "AAAA")
    target = target.replace("XX", "BB")

    if 'X' in target:
        print(-1)
    else:
        print(target)

solve()