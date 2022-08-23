import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
li = list()
i = 0
while True:
    i+=1
    if n <= i**2 <= m:
        li.append(i**2)
    elif i**2 > m:
        break

if len(li) > 0:
    print(sum(li))
    print(li[0])
else:
    print(-1)