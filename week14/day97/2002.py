## 2002
import sys
input = sys.stdin.readline

N = int(input())
res = 0
enter, out = dict(), []
for i in range(N):
	car = input()
	enter[car] = i
for _ in range(N):
	car = input()
	out.append(car)
 
for i in range(N-1):
	for j in range(i+1, N):
		if enter[out[i]] > enter[out[j]]:
			res += 1
			break
print(res)