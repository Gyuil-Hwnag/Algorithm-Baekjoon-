import sys
input = sys.stdin.readline
s = input().strip()

res = set()
for i in range(1, len(s)+1):
    for j in range(0, len(s)-i+1):
        res.add(s[j:j+i])
print(len(res))