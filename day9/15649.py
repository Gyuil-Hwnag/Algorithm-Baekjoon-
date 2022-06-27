import sys
input = sys.stdin.readline

n, m = map(int, input().split())

res = list()
def DFS():
  if len(res) == m:
    r = ""
    for i in res:
        r = r+str(i)+" "
    print(r)
    return

  for i in range(1, n + 1):
    if i in res:
      continue
    res.append(i)
    DFS()
    res.pop()

DFS()