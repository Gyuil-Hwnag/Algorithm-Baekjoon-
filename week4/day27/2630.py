import sys
input = sys.stdin.readline

n = int(input())
board = list(list(map(int, input().split())) for _ in range(n))
res = list()

def RECURSIVE(x, y, n) :
  color = board[x][y]
  for i in range(x, x+n) :
    for j in range(y, y+n) :
      if color != board[i][j] :
        RECURSIVE(x, y, n//2)
        RECURSIVE(x, y+n//2, n//2)
        RECURSIVE(x+n//2, y, n//2)
        RECURSIVE(x+n//2, y+n//2, n//2)
        return
  if color == 0 :
    res.append(0)
  else :
    res.append(1)

RECURSIVE(0,0,n)
print(res.count(0))
print(res.count(1))