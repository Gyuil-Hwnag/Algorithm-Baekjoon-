import sys
input = sys.stdin.readline

def Solve():
    global num
    print(sum(num)//5)
    print(num[2])

num = list(int(input()) for _ in range(5))
num.sort()
Solve()