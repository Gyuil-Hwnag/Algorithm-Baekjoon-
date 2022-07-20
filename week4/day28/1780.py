import sys
input = sys.stdin.readline

n = int(input())
paper = list(list(map(int, input().split())) for _ in range(n))
res = [0]*3

def RECURSIVE(x, y, n):
    global res
    num = paper[y][x]
    for yy in range(y, y+n):
        for xx in range(x, x+n):
            if paper[yy][xx] != num:
                for i in range(3):
                    for j in range(3):
                        RECURSIVE(x+j*(n//3), y+i*(n//3), n//3)
                return
    if num == -1:
        res[0]+=1
    elif num == 0:
        res[1]+=1
    else:
        res[2]+=1

RECURSIVE(0, 0, n)
for i in res:
    print(i)