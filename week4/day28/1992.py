import sys
input = sys.stdin.readline

n = int(input())
board = list(list(map(int, input().rstrip())) for _ in range(n))

def RECURSIVE(x, y, n):
    check = board[x][y]
    # print("x: %d y: %d n: %d check: %d" %(x, y, n, check))
    # print()
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != board[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n//2
        RECURSIVE(x, y, n)  # 오른쪽 위
        RECURSIVE(x, y+n, n)  # 왼쪽 위
        RECURSIVE(x+n, y, n)  # 오른쪽 아래
        RECURSIVE(x+n, y+n, n)  # 왼쪽 아래
        print(")", end='')
    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')

RECURSIVE(0, 0, n)