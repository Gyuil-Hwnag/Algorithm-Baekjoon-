## 17173
import sys
input = sys.stdin.readline

def solve():
    res = 0
    for i in range(1, M+1, 1):
        for num in nums:
            if i%num == 0:
                res+=i
                break
    return res

M, K = map(int, input().split())
nums = list(map(int, input().split()))
print(solve())