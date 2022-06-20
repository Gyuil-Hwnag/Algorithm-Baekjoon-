h, m = map(int, input().split())
num = int(input())

if m+num>=60:
    h = h+(m+num)//60
    m = (m+num)%60
    if h >= 24:
        h = h%24
else:
    m = m+num
print("%d %d" %(h, m))