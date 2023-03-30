## 17618
import sys
input = sys.stdin.readline

def solve():
    global target
    res = 0
    for i in range(1, target+1):
        s = str(i)
        num = 0
        for c in s:
            num = num+int(c)
        if i%num == 0:
            res+=1
    return res

target = int(input())
result = solve()
print(result)