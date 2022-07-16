import sys
input = sys.stdin.readline

st = input().rstrip()
slist = [[0]*26]
slist[0][ord(st[0])-97] = 1
for i in range(1, len(st)):
    num = ord(st[i])-97
    slist.append(slist[i-1][:])
    slist[i][num] += 1

n = int(input())
for _ in range(n):
    c, s, e = list(input().split())
    c = ord(c)-97
    s = int(s)
    e = int(e)
    if s == 0:
        num = slist[e][c]
    else:
        num = slist[e][c] - slist[s-1][c]
    print(num)