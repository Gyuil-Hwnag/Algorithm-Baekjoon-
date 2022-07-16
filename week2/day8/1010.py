import sys
input = sys.stdin.readline

def combi(a, b):
    res = 1
    for i in range(a, a-b, -1):
        res*=i
    for i in range(b, 1, -1):
        res = res//i
    return res

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    print(combi(m, n))