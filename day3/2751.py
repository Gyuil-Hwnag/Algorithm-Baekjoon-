import sys
n = int(input())
num = list()
for _ in range(n):
    num.append(int(sys.stdin.readline()))

# num.sort()
for i in range(n):
    for j in range(i+1, n):
        if num[i] > num[j]:
            num[i], num[j] = num[j], num[i]

for i in num:
    sys.stdout.write(str(i)+'\n')