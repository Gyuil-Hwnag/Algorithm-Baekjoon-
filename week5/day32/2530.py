import sys
input = sys.stdin.readline

h, m, s = map(int, input().split())
n = int(input())

def TIME(h, m , s, n):
    s = s+n
    if s>=60:
        m = m+(s//60)
        s = s%60
    if m>=60:
        h = h+(m//60)
        m = m%60
    if h>=24:
        h = h%24
    return h, m, s

print("%d %d %d" %(TIME(h, m, s, n)))