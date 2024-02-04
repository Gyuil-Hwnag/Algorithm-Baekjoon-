## 14065
import sys
input = sys.stdin.readline

x = float(input())
ans = 100.0 / ((1.609344 / 3.785411784) * x)
print("%.6f" % ans)