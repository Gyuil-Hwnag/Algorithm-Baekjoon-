import sys
input = sys.stdin.readline

n, l = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
# for i in board:
#     print(i)

def CHECK(line):
    for i in range(1, n):
        if abs(line[i] - line[i-1]) > 1:
            return False
        if line[i] < line[i-1]:
            for j in range(l):
                if i+j>=n or line[i] != line[i+j] or res[i+j]:
                    return False
                if line[i] == line[i+j]:
                    res[i+j] = True
        elif line[i] > line[i-1]:
            for j in range(l):
                if i-j-1 < 0 or line[i-1] != line[i-j-1] or res[i-j-1]:
                    return False
                if line[i-1] == line[i-j-1]:
                    res[i-j-1] = True
    return True

cnt = 0
for i in range(n):
    res = [False]*n
    if CHECK([board[i][j] for j in range(n)]):
        cnt+=1

for j in range(n):
    res = [False]*n
    if CHECK([board[i][j] for i in range(n)]):
        cnt+=1
print(cnt)