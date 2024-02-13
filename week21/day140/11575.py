## 11575

import sys
input = sys.stdin.readline

t = input()
for _ in range(int(t)):
    a, b = map(int, input().split())
    str = input().strip()
    res = ''.join([chr((a * (ord(char) - 65) + b) % 26 + 65) for char in str])
    print(res)