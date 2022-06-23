import sys
input = sys.stdin.readline
a, b = map(int, input().split())
alist = set(map(int, input().split()))
blist = set(map(int, input().split()))

cha = list(alist-blist) + list(blist-alist)
print(len(cha))