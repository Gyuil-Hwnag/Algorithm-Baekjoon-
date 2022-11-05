import sys
input = sys.stdin.readline

def SOLVE():
    global N
    res = 0
    for _ in range(N):
        x, y = map(int, input().split())
        for i in range(x, x+10):
            for j in range(y, y+10):
                paper[i][j] = 1

    for row in paper:
        res += row.count(1)
    
    return res

N = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]

print(SOLVE())