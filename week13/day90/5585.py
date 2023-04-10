## 5585
import sys
input = sys.stdin.readline

nums = [500, 100, 50, 10, 5, 1]
target = 1000-int(input())

def dp():
    global target
    res = 0
    for num in nums:
        coin = (target//num)
        if coin > 0:
            res = res+coin
            target = target-(num*coin)
    else:
        return res

print(dp())