import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m, c = map(int, input().split())
    print("You get "+str(m//c)+" piece(s) and your dad gets "+str(m%c)+" piece(s).")