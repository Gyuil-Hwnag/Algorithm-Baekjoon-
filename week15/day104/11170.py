## 11170
import sys
input = sys.stdin.readline

def Solve():
    global n, m
    res = 0
    for i in range(n, m+1):
        s = str(i)
        for j in s:
            if j=='0':
                res+=1
    print(res)

cnt = int(input())
for _ in range(cnt):
    n, m = map(int, input().split())
    Solve()