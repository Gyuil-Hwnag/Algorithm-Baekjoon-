# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 
# 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

# 3
# 21 Junkyu
# 21 Dohyun
# 20 Sunyoung

# 20 Sunyoung
# 21 Junkyu
# 21 Dohyun

import sys
n = int(sys.stdin.readline())
p = list()
for i in range(n):
    p.append(sys.stdin.readline().split())

p.sort(key = lambda x: int(x[0]))

for i in p:
    print(i[0], i[1])