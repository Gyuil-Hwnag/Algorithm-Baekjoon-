import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    cloth = dict()
    m = int(input())
    for _ in range(m):
        a, b = input().split()
        if b not in cloth.keys():
            cloth[b]=1
        else:
            cloth[b] = cloth[b]+1
    res = 1
    for i in cloth.keys():
        res = res*(cloth[i]+1)
    print(res-1)