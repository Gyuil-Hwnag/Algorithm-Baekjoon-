import sys
input = sys.stdin.readline

def Solve():
    num = [1]*10
    for _ in range(n-1):
        for j in range(1, 10):
            num[j] += num[j-1]
    return sum(num)%10007

n = int(input())
print(Solve())