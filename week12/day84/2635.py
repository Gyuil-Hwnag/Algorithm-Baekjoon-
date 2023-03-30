## 2635
import sys
from collections import deque
input = sys.stdin.readline

def dfs():
    global n, resList
    for i in range(1, n+1):
        tempList = [n, i]

        targetIdx = 1
        while True:
            next = tempList[targetIdx-1] - tempList[targetIdx]
            if next < 0:
                break
            tempList.append(next)
            targetIdx += 1
        
        if len(tempList) > len(resList):
            resList =  tempList

n = int(input())
resList = list()
dfs()
res = ""
for s in resList:
    res = res + str(s) + " "
print(len(resList))
print(res)