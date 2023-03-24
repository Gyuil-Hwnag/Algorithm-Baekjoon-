## 13909
import sys
input = sys.stdin.readline

def solve(peoples):
    res = 1
    for i in range(2, int(peoples**(0.5)+1)):
        if i**2 <= peoples:
            res+=1
    return res

peoples = int(input())
print(solve(peoples = peoples))