## 18868
import sys
input = sys.stdin.readline

def solve():
    res = 0
    for _ in range(m):
        for i in range(m):
            sortList = sorted(plants[i])
            idx = []
            for j in plants[i]:
                idx.append(sortList.index(j))
            plants[i] = idx

    for i in range(m - 1):
        for j in range(i + 1, m):
            if plants[i] == plants[j]:
                res += 1
    return res

m, n = map(int, input().split())
plants = [list(map(int, input().split())) for _ in range(m)]

print(solve())