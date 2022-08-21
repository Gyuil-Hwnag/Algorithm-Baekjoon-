import sys
input = sys.stdin.readline

odd = list()
even = list()
for _ in range(7):
    n = int(input())
    if n%2 == 0:
        even.append(n)
    else:
        odd.append(n)

if len(odd)>0:
    odd.sort()
    print(sum(odd))
    print(odd[0])
else:
    print(-1)