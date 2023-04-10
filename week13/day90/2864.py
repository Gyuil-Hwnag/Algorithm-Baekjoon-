## 2864
import sys
input = sys.stdin.readline

a,b = input().split()

def solve(a, b):
    maxi = int(a.replace('5','6')) + int(b.replace('5','6'))
    mini = int(a.replace('6','5'))+ int(b.replace('6','5'))
    print(mini, maxi)

solve(a, b)