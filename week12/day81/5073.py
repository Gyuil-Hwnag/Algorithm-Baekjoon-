## 5073
import sys
input = sys.stdin.readline

def solve(angles):
    if len(set(angles)) == 1:
        return "Equilateral"
    elif len(set(angles)) == 2:
        return "Isosceles"
    else:
        return "Scalene"

while True:
    angles = list(map(int, input().split()))
    if sum(angles) == 0:
        break

    if sum(angles) - (2*max(angles)) <= 0:
        print("Invalid")
    else:
        print(solve(angles))