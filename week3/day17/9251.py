import sys
input = sys.stdin.readline

a = ' '+input().rstrip()
b = ' '+input().rstrip()
la = len(a)
lb = len(b)

dy = list([0]*lb for _ in range(la))

for i in range(1, la):
    for j in range(1, lb):
        if a[i] == b[j]:
            dy[i][j] = dy[i-1][j-1]+1
        else:
            dy[i][j] = max(dy[i-1][j], dy[i][j-1])

print(dy[-1][-1])
# for i in range(len(dy)):
#     print(dy[i])


# 앞에 빈 문자열 추가했을 때와 안했을때 그래프 차이 보기
# a = input().rstrip()
# b = input().rstrip()
# la = len(a)
# lb = len(b)

# dy = list([0]*lb for _ in range(la))

# for i in range(la):
#     for j in range(lb):
#         if a[i] == b[j]:
#             dy[i][j] = dy[i-1][j-1]+1
#         else:
#             dy[i][j] = max(dy[i-1][j], dy[i][j-1])

# for i in range(len(dy)):
#     print(dy[i])

