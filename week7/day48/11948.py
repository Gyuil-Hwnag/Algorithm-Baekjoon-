import sys
input = sys.stdin.readline

num1 = list()
num2 = list()

for _ in range(4):
    num1.append(int(input()))

for _ in range(2):
    num2.append(int(input()))
num1.sort(reverse=True)
num2.sort(reverse=True)
print(num1[0]+num1[1]+num1[2]+num2[0])