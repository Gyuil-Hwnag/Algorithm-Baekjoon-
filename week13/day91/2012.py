## 2012
import sys
input = sys.stdin.readline

N = int(input())
peoples = list()
for _ in range(N):
    peoples.append(int(input()))
peoples.sort()

res = 0
for i in range(N):
    res = res + abs(i+1-peoples[i])
print(res)