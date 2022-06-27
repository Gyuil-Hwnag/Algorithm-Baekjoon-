import sys
input = sys.stdin.readline

n = int(input())
num = 1
for i in range(n, 1, -1):
    num *= i

res = list(str(num))
cnt = 0
for i in range(len(res)-1, -1, -1):
    if res[i] == '0':
        cnt+=1
    else:
        break
print(cnt)