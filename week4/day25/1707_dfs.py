import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def DFS(s, group):
    ch[s] = group
    for i in graph[s]:
        if ch[i] == 0:
            if not DFS(i, -group):
                return False
        elif ch[i] == group:
            return False
    return True

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    ch = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    res = True
    for i in range(1, v+1):
        if ch[i] != 0:
            continue
        if not res:
            break
        res = DFS(i, 1)
    
    if res:
        print("YES")
    else:
        print("NO")