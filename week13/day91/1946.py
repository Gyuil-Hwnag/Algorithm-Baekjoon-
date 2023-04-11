## 1946
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    peoples = list()
    for _ in range(N):
        peoples.append(list(map(int, input().split())))
    
    peoples.sort()
    target = peoples[0][1]
    res = 1
    for i in range(N):
        if target > peoples[i][1]:
            res += 1
            target = peoples[i][1]
    print(res)