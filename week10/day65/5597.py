import sys
input = sys.stdin.readline

def SOLVE(req):
    for _ in range(28):
        req[int(input())] = 1
    for i in range(1, 31):
        if req[i] == 0:
            print(i)

people = [0 for _ in range(31)]
SOLVE(req=people)