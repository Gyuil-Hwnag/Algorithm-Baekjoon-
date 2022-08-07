import sys
input = sys.stdin.readline

def Num(str):
    if str == "black":
        return 0
    elif str == "brown":
        return 1
    elif str == "red":
        return 2
    elif str == "orange":
        return 3
    elif str == "yellow":
        return 4
    elif str == "green":
        return 5
    elif str == "blue":
        return 6
    elif str == "violet":
        return 7
    elif str == "grey":
        return 8
    else:
        return 9

def Last(str):
    return 10**Num(str)

one = input().rstrip()
two = input().rstrip()
three = input().rstrip()

print(int(str(Num(one))+str(Num(two)))*Last(three))