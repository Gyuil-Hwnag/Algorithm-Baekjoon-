import sys
input = sys.stdin.readline

def SOLVE(type, c, board):
    global scores
    r = 0
    # 블록 내리기
    while True:
        if type == 2:
            if r == 5 or board[r + 1][c] or board[r + 1][c + 1]:
                break
            else:
                r += 1
        else:
            if r == 5 or board[r + 1][c]:
                break
            else:
                r += 1

    board[r][c] = 1
    if type == 2:
        board[r][c + 1] = 1
    elif type == 3:
        board[r - 1][c] = 1

    # 줄 없애기
    full_row = []
    for i in range(5, -1, -1):
        if sum(board[i]) == 4:
            full_row.append(i)
            scores += 1

    pop_row_num = len(full_row)
    for idx in full_row:
        board.pop(idx)

    for _ in range(pop_row_num):
        board.insert(0, [0]*4)

    # 0, 1행 확인
    while True:
        if sum(board[1]) != 0:
            board.pop()
            board.insert(0, [0]*4)
        else:
            break

N = int(input())
blocks = [list(map(int, input().split())) for _ in range(N)]
scores = 0
green_board = [[0 for _ in range(4)] for _ in range(6)]
blue_board = [[0 for _ in range(4)] for _ in range(6)]

for type, x, y in blocks:
    SOLVE(type, y, green_board)

    if type == 1:
        SOLVE(type, 3 - x, blue_board)
    elif type == 2:
        SOLVE(3, 3 - x, blue_board)
    elif type == 3:
        SOLVE(2, 3 - x - 1, blue_board)

total_block = 0
for i in range(6):
    total_block += sum(green_board[i])
    total_block += sum(blue_board[i])

print(scores, total_block, sep="\n")