num = [0]*7
a, b, c = map(int, input().split())
num[a] += 1
num[b] += 1
num[c] += 1

i = max(num)
if i == 3:
    sum = 10000+num.index(i)*1000
elif i == 2:
    sum = 1000+num.index(i)*100
else:
    sum = max(a, b, c)*100

print(sum)