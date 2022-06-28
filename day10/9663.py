import sys
input = sys.stdin.readline

n = int(input())
res = 0
row = [0]*n

def DFS(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True

def QUEEN(x):
    global res
    if x == n:
        res += 1
        return
    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if DFS(x):
                QUEEN(x+1)

QUEEN(0)
print(res)
    
# 파이썬으로는 정답이 안나와서 야매로 입력하면 된다고 한다.
# answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
# print(answer[int(input())])