## 17103
import sys
input = sys.stdin.readline

def getPrimeList(num):
    primeList = [True for _ in range(num+1)]
    for i in range(2, int(num**0.5)+1, 1):
        if primeList[i]:
            for j in range(i+i, num+1, i):
                primeList[j] = False
    return primeList

def Solve():
    global primeList
    for i in targets:
        res = 0
        for j in range(2, i//2+1, 1):
            if primeList[j] and primeList[i-j]:
                res+=1
        print(res)

n = int(input())
targets = [int(input()) for _ in range(n)]
maxTarget = max(targets)
primeList = getPrimeList(maxTarget)
Solve()