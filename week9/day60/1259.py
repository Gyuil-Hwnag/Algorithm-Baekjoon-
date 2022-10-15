import sys
input = sys.stdin.readline

def SOLVE(str):
    n = len(str)
    ch = True
    for i in range(n//2):
        if str[i] != str[n-1-i]:
            ch = False
            break
    return ch

def RESULT(res):
    if res:
        print("yes")
    else:
        print("no")

while True:
    str = input().rstrip()
    if str == "0":
        break
    else:
        RESULT(SOLVE(str))