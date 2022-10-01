import sys
input = sys.stdin.readline

str = input().rstrip()
alplhabet = [0 for _ in range(26)]

for i in str:
    n = ord(i)-97
    alplhabet[n]+=1

for i in alplhabet:
    print(i, end=' ')