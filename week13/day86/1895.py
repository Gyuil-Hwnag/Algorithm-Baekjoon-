## 1895
import sys
input = sys.stdin.readline

def solve():
    global res, target
    for x in range(R-2):
        for y in range(C-2):
            temp = list()
            for xx in range(x, x+3):
                for yy in range(y, y+3):
                    temp.append(I[xx][yy])
            temp.sort()
            if target <= temp[4]:
                res+=1

R, C = map(int, input().split())
I = list()
for _ in range(R):
    I.append(list(map(int, input().split())))

target = int(input())
res = 0
solve()
print(res)