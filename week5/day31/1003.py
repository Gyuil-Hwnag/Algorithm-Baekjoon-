import sys
input = sys.stdin.readline

zero = [1, 0, 1]
one = [0, 1, 1]

def Fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print("%d %d" %(zero[num], one[num]))

t = int(input())
for _ in range(t):
    Fibonacci(int(input()))