import sys
input = sys.stdin.readline
n, k = map(int, input().split())
p = 1000000007

# 계산식으로 했더니 에러발생
# res = 1
# t = max(n-k, k)
# for i in range(n, t, -1):
#     res = (res*i)%p
#     res = ((res/(i-n-1))*-1)
#     # print(res)

# res = int(res)
# print(res)

def divide(a,b):
    # print("a: %d, b: %d" %(a, b))
    if b == 1:
        return a%p
    elif b%2 == 1:
        return divide((a**2)%p, b//2)*a%p
    else:
        return divide((a**2)%p, b//2)

a = 1
b = 1
t = min(n-k, k)

for i in range(t):
    a = a*(n-i)%p
    b = b*(t-i)%p
print((a*divide(b,p-2))%p)

#페르마의 소정리
# (A/B) % p
# = A * B^-1 % p
# = A * B^-1 * B^p-1 % p
# = A * B^p-2 % p
# = (A % p) * (B^p-2 % p) % p