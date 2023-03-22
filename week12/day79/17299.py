## 17299
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
numCount = Counter(nums)
res = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and numCount[nums[stack[-1]]] < numCount[nums[i]]:
            res[stack.pop()] = nums[i]
    stack.append(i)

print(*res)