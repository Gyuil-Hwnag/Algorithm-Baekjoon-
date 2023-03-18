## 2485
import sys
from math import gcd

input = sys.stdin.readline

n = int(input())
start = int(input())

trees = list()
for i in range(n-1):
    tree = int(input())
    trees.append(tree - start)
    start = tree

g = trees[0]
for i in range(1, len(trees)):
    g = gcd(g, trees[i])

res = 0
for size in trees:
    res += size//g -1
print(res)