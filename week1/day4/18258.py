from collections import deque
import sys

st = deque()
def S(s, n):
    if s=="push":
        st.append(n)
    elif s=="pop":
        if len(st) == 0:
            print(-1)
        else:
            print(st.popleft())
    elif s=="size":
        print(len(st))
    elif s=="empty":
        if len(st)==0:
            print(1)
        else:
            print(0)
    elif s=="front":
        if len(st)==0:
            print(-1)
        else:
            print(st[0])
    elif s=="back":
        if len(st)==0:
            print(-1)
        else:
            print(st[-1])

n = int(sys.stdin.readline())
for i in range(n):
    line = sys.stdin.readline().split()
    if line[0] == 'push':
        S(line[0], line[1])
    else:
        S(line[0], 0)
