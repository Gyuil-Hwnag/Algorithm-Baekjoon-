import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort()

m = int(input())
ch = list(map(int, input().split()))

def DFS(lt, rt, c):
    if lt>rt:
        print(0)
        return
    mid = (lt+rt)//2
    # print("mid : %d" %(mid))
    if num[mid] == c:
        # print("num : %d" %(c))
        print(1)
    else:
        if num[mid]>c:
            DFS(lt, mid-1, c)
        else:
            DFS(mid+1, rt, c)

for i in ch:
    DFS(0, n-1, i)