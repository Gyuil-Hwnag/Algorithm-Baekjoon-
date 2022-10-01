import sys

input = sys.stdin.readline
N = int(input())
result = 1

start = 1
end = 2
sumNum = 3

while start <= N//2:
    if sumNum < N:
        end += 1
        sumNum += end
    elif sumNum > N:
        sumNum -= start
        start += 1
    else:
        result += 1
        end += 1
        sumNum += end
        sumNum -= start
        start += 1

print(result)