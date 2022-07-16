import sys
input = sys.stdin.readline

n = int(input())
graphs = list(int(input()) for _ in range(n))

dy = [0]*n
if n == 1:
    print(graphs[0])
elif n==2:
    print(graphs[1]+graphs[0])
else: 
    dy[0] = graphs[0]
    dy[1] = graphs[1]+graphs[0]
    dy[2] = max(dy[1], graphs[2]+graphs[1], graphs[0]+graphs[2])
    for i in range(3, n):
        dy[i] = max(dy[i-1], dy[i-3]+graphs[i-1]+graphs[i], dy[i-2]+graphs[i])

    print(max(dy))