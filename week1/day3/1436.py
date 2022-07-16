n = int(input())

cnt = 0
num = 666
while True:
    s = str(num)
    idx = s.find('666')
    if idx != -1:
        cnt+=1

    if cnt == n:
        break
    else:
        num+=1
print(s)