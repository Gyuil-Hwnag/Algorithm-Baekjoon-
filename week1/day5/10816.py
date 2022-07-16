import sys
n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
my = list(map(int, sys.stdin.readline().split()))

ch = {}
for i in card:
    if i in ch:
        ch[i] += 1
    else:
        ch[i] = 1

for i in my:
    result = ch.get(i)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")