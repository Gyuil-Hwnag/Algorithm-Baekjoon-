## 1252

import sys
input = sys.stdin.readline

A, B = map(str, input().split())
A = int(A, 2)
B = int(B, 2)
C = A + B

print(bin(C)[2:])