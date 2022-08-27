import sys
input = sys.stdin.readline

n = int(input())
s = 0
for _ in range(n):
    s+=int(input())
if s/n>=0.5:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")