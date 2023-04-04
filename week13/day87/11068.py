## 11068
import sys
input = sys.stdin.readline

def solve(num):
    res = 0
    for na in range(2, 65):
        naList = list()
        temp = num
        while temp != 0:
            naList.append(temp%na)
            temp = temp//na
        
        for idx in range(len(naList)//2):
            if(naList[idx] != naList[-1-idx]):
                res += 1
                break
    
    if res == 63:
        return 0
    else:
        return 1

T = int(input())
for _ in range(T):
    print(solve(int(input())))