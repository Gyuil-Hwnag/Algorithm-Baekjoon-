import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
ch = list(map(int, input().split()))

# 최대 최소 범위 잘 설정하기
# maxi = -2147000
# mini = 2147000
maxi = -1000000001
mini = 1000000001

op = list()
res = num[0]
def DFS(L):
    global res
    global maxi
    global mini
    if L == n:
        maxi = max(maxi, res)
        mini = min(mini, res)
        return
    else:
        tmp = res
        for i in range(4):
            if ch[i]!=0:
                if i==0:
                    res += num[L]
                elif i==1:
                    res -= num[L]
                elif i==2:
                    res*=num[L]
                else:
                    if res >= 0:
                        res //= num[L]
                    else:
                        res = (-res // num[L]) * -1
                ch[i]-=1
                DFS(L+1)
                res = tmp
                ch[i]+=1
DFS(1)
print(maxi)
print(mini)