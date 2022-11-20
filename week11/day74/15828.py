from ntpath import join
import sys
from collections import deque
input = sys.stdin.readline

def Solve():
    global size
    dq = deque()
    while(True):
        n = int(input())
        if n==-1:
            break
        if len(dq)>=size and n!=0:
            continue
        elif n==0:
            dq.popleft()
        else:
            dq.append(n)

    if dq:
        print(*dq)
    else: 
        print("empty")

size = int(input())
Solve()