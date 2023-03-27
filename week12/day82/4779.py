## 4479
import sys
input = sys.stdin.readline

# 남은 횟수, 시작점, 끝점
def dfs(n, i, j):  
    if n == 0:
        return
    cnt = (j-i+1) // 3

    # Left
    dfs(n-1, i, i+cnt-1)
    # Mid
    for k in range(i + cnt, i + cnt*2):
        answer[k] = ' '
    # Right
    dfs(n-1, i + cnt*2, i + cnt*3 - 1)

while True:
    try:
        n = int(input())
        answer = ['-'] * (3 ** n)
        dfs(n, 0, 3 ** n - 1)
        print(''.join(answer))
    except:
        break
