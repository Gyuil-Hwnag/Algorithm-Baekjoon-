import sys
input = sys.stdin.readline

n ,m = map(int, input().split())
def twoOrfinve(n, k):
    cnt = 0
    while n!=0:
        n = n//k
        cnt+=n
    return cnt

if m != 0:
    two = twoOrfinve(n,2)-twoOrfinve(m,2)-twoOrfinve(n-m,2)
    five = twoOrfinve(n,5)-twoOrfinve(m,5)-twoOrfinve(n-m,5)
    print(min(two, five))
else:
    print(0)