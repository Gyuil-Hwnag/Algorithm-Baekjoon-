import sys
input = sys.stdin.readline

n = input()
n = int(n, 8)
print(bin(n)[2:])