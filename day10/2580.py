# python 말고 pypy로 제출하기 <- 안그러면 시간초과 무조건 남
import sys
input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def check(i, j):
    ch = [1,2,3,4,5,6,7,8,9]  
    for k in range(9):
        if sudoku[i][k] in ch:
            ch.remove(sudoku[i][k])
        if sudoku[k][j] in ch:
            ch.remove(sudoku[k][j])

    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in ch:
                ch.remove(sudoku[p][q])
    return ch

res = False
def DFS(x):
    global res
    if res: #이미 답이 출력된 경우
        return
        
    if x == len(zeros): #마지막 0까지 다 채웠을 경우
        for row in sudoku:
            print(*row)
        res = True #답 출력
        return
        
    else:    
        (i, j) = zeros[x]
        checknum = check(i, j) #유망한 숫자들을 받음
        
        for num in checknum:
            sudoku[i][j] = num #유망한 숫자 중 하나를 넣어줌
            DFS(x + 1) #다음 0으로 넘어감
            sudoku[i][j] = 0 #초기화 (정답이 없을 경우를 대비)
DFS(0)