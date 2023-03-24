## 2720
import sys
input = sys.stdin.readline

QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1

def solve(target):
    res = [0 for _ in range(4)]
    if target // QUARTER >= 0:
        res[0] = target // QUARTER
        target = target%QUARTER
    
    if target % DIME >= 0:
        res[1] = target // DIME
        target = target%DIME

    if target % NICKEL >= 0:
        res[2] = target // NICKEL
        target = target%NICKEL

    res[3] = target // PENNY
    return res

T = int(input())
for i in range(T):
    coins = int(input())
    result = ' '.join(str(s) for s in solve(coins))
    print(result)
