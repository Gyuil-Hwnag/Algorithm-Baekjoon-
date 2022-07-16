import sys
input = sys.stdin.readline

num1 = 0

def Fibo(n):
    global num1
    if n==1 or n==2:
        num1+=1
        return 1
    else:
        return Fibo(n-1)+Fibo(n-2)

num = int(input())
Fibo(num)
print(num1, num-2)