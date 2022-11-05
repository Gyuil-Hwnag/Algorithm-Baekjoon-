import sys
input = sys.stdin.readline

def SOLVE():
    global n, people
    res = 0 
    pcList = list(0 for _ in range(100))
    for i in people:
        if pcList[i-1] == 0:
            pcList[i-1] = 1
        else:
            res+=1
    return res

n = int(input())
people = list(map(int, input().split()))
print(SOLVE())