## 4597
import sys

input = sys.stdin.readline
while True:
    req = input()
    if req == '#':
        break
    p = req[-1]
    req = req[:-1]
    count = req.count('1')
    if p == 'e':
        if count % 2 == 0:
            req += '0'
        else:
            req += '1'
    else:
        if count % 2 == 0:
            req += '1'
        else:
            req += '0'
    print(req)