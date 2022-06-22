# set
import sys
n = int(sys.stdin.readline())
my = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

ch = [0]*m

for i in card:
    if i in my:
        print(1, end=' ')
    else:
        print(0, end=' ')

# binary
import sys
n = int(sys.stdin.readline())
my = list(map(int, sys.stdin.readline().split()))
my.sort()

m = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

def binary(num):
    l = 0
    r = n-1
    while l <= r :
        mid = (l+r)//2
        if my[mid] == num :
            return 1
        elif my[mid] > num :
            r = mid - 1
        else:
            l = mid + 1
    return 0


for i in card:
    print(binary(i), end=' ')