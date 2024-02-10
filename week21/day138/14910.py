## 14910
import sys

input = sys.stdin.readline
N = list(map(int, input().split()))
A = sorted(N)
if N == A:
    print('Good')
else:
    print('Bad')