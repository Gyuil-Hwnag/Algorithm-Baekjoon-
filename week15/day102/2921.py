## 2921
from itertools import combinations_with_replacement

n = int(input())
res = 0
for i in combinations_with_replacement(range(n+1), 2):
    res += sum(i)
print(res)