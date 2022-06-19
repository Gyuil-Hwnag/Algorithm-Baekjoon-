def DFS(n):
    res=list()
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            res.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            res.append(n[i % len(n)] * 3)
    return res
 
star = ["***", "* *", "***"]
n = int(input())
e = 0
while n != 3:
    n = int(n / 3)
    e += 1
for i in range(e):
    star = DFS(star)
for i in star:
    print(i)
