import sys
input = sys.stdin.readline
from itertools import permutations

def Solve():
    global num, n
    per = permutations(num)
    res = 0

    for i in per:
        s = 0
        for j in range(len(i)-1):
            s += abs(i[j]-i[j+1])
        res = max(s, res)
    
    print(res)

n = int(input())
num = list(map(int, input().split()))
Solve()