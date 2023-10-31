## 10823
import sys
input = sys.stdin.readline

res = ''
while True:
    try:
        tmp = input()
        res += tmp
    except EOFError:
        break

numlist = list(map(int, res.split(",")))
print(sum(numlist))