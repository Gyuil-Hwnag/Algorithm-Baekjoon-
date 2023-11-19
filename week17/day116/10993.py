## 10993
import sys
input = sys.stdin.readline

n = int(input())
row = 2 ** n - 1
col = 2 * row - 1
canvas = [[' '] * col for i in range(row)]

def draw(x, y, n) :
    row = 2 ** n - 1
    col = 2 * row - 1

    if n == 1 :
        canvas[x][y] = '*'
        return;

    if n % 2 : 
        for i in range(row-1,-1,-1) :
            canvas[x + row - i - 1][y + i] = '*'
            canvas[x + row - i - 1][y + col - 1 - i] = '*'
            if i == 0 :
                for j in range(1, col-1) :
                    canvas[x + row - 1][y + j] = '*'
        draw(x + 2 ** (n-1) - 1, y + 2 ** (n-1), n - 1)

    else :
        for i in range(row) :
            canvas[x + i][y + i] = '*'
            canvas[x + i][y + col - 1 - i] = '*'
            if i == 0 :
                for j in range(1, col-1) :
                    canvas[x][y + j] = '*'
        draw(x + 1, y + 2 ** (n-1), n - 1)

draw(0, 0, n)
for line in canvas :
    print(''.join(line).rstrip())