## 18917
import sys
input = sys.stdin.readline
n = int(input())
sum = 0
xor = 0
for i in range(n):
    oper = list(map(int, input().split()))
    if oper[0] == 1:
        sum += oper[1]
        xor = xor^oper[1]
    elif oper[0] == 2 :
        sum -= oper[1]
        xor = xor^oper[1]
    elif oper[0] == 3: print((sum))
    elif oper[0] == 4: print(xor)