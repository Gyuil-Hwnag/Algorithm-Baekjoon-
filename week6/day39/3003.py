# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개

import sys
input = sys.stdin.readline

ch = list(map(int, input().split()))
k = 1-ch[0]
q = 1-ch[1]
l = 2-ch[2]
v = 2-ch[3]
n = 2-ch[4]
p = 8-ch[5]
print("%d %d %d %d %d %d" %(k, q, l, v, n, p))