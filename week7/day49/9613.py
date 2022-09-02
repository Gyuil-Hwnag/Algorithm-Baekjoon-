import sys
import math
input = sys.stdin.readline

for _ in range(int(input())):
    s = list(map(int,input().split()))
    n, nums, r = s[0], s[1:], 0
    
    for i in range(n-1):
        for j in range(i+1,n):
            r += math.gcd(nums[i],nums[j])
    print(r)