import sys
input = sys.stdin.readline

a, b, c = map(int, input().strip().split())
if a+b == c:
    print(str(a)+"+"+str(b)+"="+str(c))
elif a-b == c:
    print(str(a)+"-"+str(b)+"="+str(c))
elif a*b == c:
    print(str(a)+"*"+str(b)+"="+str(c))
elif a%b == 0 and a//b == c:
    print(str(a)+"/"+str(b)+"="+str(c))
elif a == b+c:
    print(str(a)+"="+str(b)+"+"+str(c))
elif a == b-c:
    print(str(a)+"="+str(b)+"-"+str(c))
elif a == b*c:
    print(str(a)+"="+str(b)+"*"+str(c))
elif b%c == 0 and a == b//c:
    print(str(a)+"="+str(b)+"/"+str(c))