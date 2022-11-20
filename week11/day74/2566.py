#2566
import sys
input = sys.stdin.readline

def Solve():
    global num
    res = 0
    resX, resY = 0, 0
    for row in range(9):
        for col in range(9):
            if num[row][col] >= res:
                res = num[row][col]
                resX = row+1
                resY = col+1
    print(res)
    print(resX, resY)

num = list(list(map(int, input().split())) for _ in range(9))
Solve()