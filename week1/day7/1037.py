import sys

input = sys.stdin.readline

# 더 오래걸림
# n = int(input())
# maxi = 0
# num = list(map(int, input().split()))
# min = max(num)

# for i in num:
#     if min>i:
#         min = i
#     if maxi<i:
#         maxi = i

# print(min*maxi)

# 더 빠름
n = int(input())
num = list(map(int, input().split()))
num.sort()
print(num[0]*num[-1])