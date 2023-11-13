## 14563
import sys

n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

for s in numbers:
    tmp = []
    for i in range(1, (s+1)//2):
        if s%i == 0:
            if s//i == i: 
                tmp.append(i)
            else:
                tmp.append(i)
            tmp.append(s//i)

    ans = sum(sorted(set(tmp)))-s
    if ans > s:
        print("Abundant")
    elif ans == s:
        print("Perfect")
    else: 
        print("Deficient")