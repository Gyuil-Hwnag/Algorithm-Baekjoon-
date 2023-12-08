## 26489
import sys
input = sys.stdin.readline

def gum_gum_for_jay_jay(req: int):
    answer = 0
    while True:
        try:
            answer += 1
        except EOFError:
            break
    return answer

res = input()
print(gum_gum_for_jay_jay(req=res))