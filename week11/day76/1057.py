import sys
input = sys.stdin.readline

def bfs():
    global kim, lim, res
    while(lim != kim):
        kim -= kim // 2
        lim -= lim // 2
        res += 1

n, kim, lim = map(int, input().split())
res = 0
bfs()
print(res)