## 4134
import sys
import math
input = sys.stdin.readline

def Solve(num):
    if num==0 or num==1:
        return 2
    while True:
        for i in range(2, int(math.sqrt(num)+1), 1):
            if num%i == 0:
                num = num+1
                break
        else:
            return num

n = int(input())
for i in range(n):
    num = int(input())
    print(Solve(num = num))