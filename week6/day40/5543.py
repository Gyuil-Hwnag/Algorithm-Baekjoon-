import sys
input = sys.stdin.readline

ham = list(int(input().rstrip()) for _ in range(3))
drink = list(int(input().rstrip()) for _ in range(2))

mini = 4000
for i in range(3):
    for j in range(2):
        s = ham[i]+drink[j]-50
        mini = min(s, mini)
print(mini)