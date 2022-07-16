import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
ch = [0]
for i in num:
    # print(ch)
    lt = 0
    rt = len(ch)-1
    while lt<=rt:
        mid = (lt+rt)//2
        if i > ch[mid]:
            lt = mid+1
        else:
            rt = mid-1
    if lt > len(ch)-1:
        # print("lt : %d i : %d" %(lt, i))
        ch.append(i)
    else:
        # print("lt : %d i : %d" %(lt, i))
        # print(ch)
        ch[lt] = i
        # print(ch)
print(len(ch)-1)