import sys
input = sys.stdin.readline

while True:
    slist = list(map(int, input().split()))
    if slist[0] == 0:
        break
    
    slist.append(0)
    res = 0
    stack = [[0, 0]]
    
    for i in range(1, slist[0] + 2):
        while stack[-1][1] > slist[i]:
            tlist = stack.pop()
            tmp = 0
            while stack[-1][1] == tlist[1]:
                stack.pop()
            tmp = max((i-1 - stack[-1][0]) * tlist[1], (i-tlist[0]) * tlist[1])
            if tmp > res:
                res = tmp
        stack.append([i, slist[i]])
    print(res)