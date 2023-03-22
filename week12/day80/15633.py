## 15633
import sys
input = sys.stdin.readline

n = int(input())
res = sum([i for i in range(1, n+1) if n%i==0])*5-24
print(res)