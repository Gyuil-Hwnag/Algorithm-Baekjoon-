import sys
input = sys.stdin.readline

n = int(input())
def SOLVE(res):
    print("Distances: ", end='')
    for i in res:
        print(i, end=' ')
    print()

for _ in range(n):
    res = list()
    base, target = map(str, input().split())
    for i in range(len(target)):
        res.append((ord(target[i])-ord(base[i])+26)%26)
    SOLVE(res)