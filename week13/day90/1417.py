## 1417
import sys
input = sys.stdin.readline

n = int(input())
nums = list()
target = int(input())
for _ in range(n-1):
    nums.append(int(input()))

def solve():
    global target
    res = 0
    if n == 1:
        return res
    else:
        nums.sort(reverse=True)
        while nums[0] >= target:
            nums[0] -= 1
            target += 1
            res += 1
            nums.sort(reverse=True)
        return res

print(solve())