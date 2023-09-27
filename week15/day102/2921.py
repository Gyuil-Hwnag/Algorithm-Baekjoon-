## 2921
from itertools import combinations_with_replacement

# 입력
n = int(input())

# 중복조합
res = 0
for i in combinations_with_replacement(range(n+1), 2):
    res += sum(i)
print(res)