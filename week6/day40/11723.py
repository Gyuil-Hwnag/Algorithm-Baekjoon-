import sys
input = sys.stdin.readline

S = set()
T = int(input())
for i in range(T):
    str = input().split()
    if len(str) == 1:
        if str[0] == 'all':
            S = set([x for x in range(1, 21)])
        else:
            S = set()

    else:
        order, num = str[0], int(str[1])
        if order == 'add':
            S.add(num)
        elif order == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif order == 'remove':
            if num in S:
                S.discard(num)
        elif order == 'toggle':
            if num in S:
                S.discard(num)
            else:
                S.add(num)