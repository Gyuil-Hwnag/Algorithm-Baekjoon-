## 10101
import sys
input = sys.stdin.readline

def solve():
    global angles
    if sum(angles) != 180:
        return "Error"
    elif len(set(angles)) == 1:
        return "Equilateral"
    elif len(set(angles)) == 2:
        return "Isosceles"
    else:
        return "Scalene"

angles = [int(input()) for _ in range(3)]
print(solve())