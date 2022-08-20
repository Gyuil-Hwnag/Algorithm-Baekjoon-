import sys
input = sys.stdin.readline

n = int(input())
a, b, c = 0, 0, 0
if n//300 >= 1:
    a = n//300
    n = n%300
if n//60 >= 1:
    b = n//60
    n = n%60
c = n//10
n = n%10

if n!=0:
    print(-1)
else:
    print("%d %d %d" %(a, b, c))
