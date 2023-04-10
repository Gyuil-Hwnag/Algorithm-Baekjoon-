## 1439
import sys
input = sys.stdin.readline

target = input().strip()
res = 0
def solve():
    global res
    for i in range(len(target)-1):
        if target[i] != target[i+1]:
            res+=1
    return res

print((solve()+1)//2)