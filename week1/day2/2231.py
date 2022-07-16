n = int(input())
res = 0
for i in range(1, n):
    num = i
    nlist = list()
    while n>1:
        if num<10:
            nlist.append(num)
            break
        else:
            nlist.append(num%10)
            num = num//10
    if n == sum(nlist)+i:
        res = i
        break
print(res)