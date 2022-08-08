import sys
input = sys.stdin.readline

board = list()
for i in range(8):
    s = input().rstrip()
    board.append(list(s))

# for i in board:
#     print(i)
cnt = 0
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            if board[i][j] == 'F':
                # print("i : %d, j : %d" %(i, j))
                cnt+=1
print(cnt)