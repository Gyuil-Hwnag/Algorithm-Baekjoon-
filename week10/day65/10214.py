import sys
input = sys.stdin.readline

def SOLVE(y, k):
    if sum(y)>sum(k):
        print("Yonsei")
    elif sum(y) == sum(k):
        print("Draw")
    else:
        print("Korea")

def INPUT():
    Y = list()
    K = list()
    for _ in range(9):
        y, k = map(int, input().split())
        Y.append(y)
        K.append(k)
    SOLVE(Y, K)

T = int(input())
for _ in range(T):
    INPUT()