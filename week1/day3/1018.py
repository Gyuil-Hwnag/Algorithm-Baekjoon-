n, m = map(int, input().split())

ch = list()
for i in range(n):
    ch.append(input())

res = list()
for i in range(n):
    for j in range(m):
        if i+7<n and j+7<m:
            w = 0
            b = 0
            for x in range(i, i+8):
                for y in range(j, j+8):
                    if (x+y) % 2 == 0:
                        if ch[x][y] != 'W':
                            w += 1
                        if ch[x][y] != 'B':
                            b += 1
                    else:
                        if ch[x][y] != 'B':
                            w += 1
                        if ch[x][y] != 'W':
                            b += 1
            res.append(min(w, b))
print(min(res))
