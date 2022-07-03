from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    defi = str(input())
    n = int(input())
    num = deque(input().rstrip()[1:-1].split(","))
    ch = 0

    if n == 0:
        num = []

    for j in defi:
        if j == 'R':
            ch+=1
        if j == 'D':
            if len(num) == 0:
                print('error')
                break
            else:
                if ch%2==0:
                    num.popleft()
                else:
                    num.pop()
    else:
        if ch%2==0:
            print("["+",".join(num)+"]")
        else:
            num.reverse()
            print("["+",".join(num)+"]")