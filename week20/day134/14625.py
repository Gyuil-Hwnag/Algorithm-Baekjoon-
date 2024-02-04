## 14625
import sys
input = sys.stdin.readline

def sol(start_total, end_total, target):
    answer = 0
    while str(start_total) != str(end_total+1):
        str_hh = str(start_total//60)
        str_mm = str(start_total % 60)
        if len(str_mm) == 1:
            str_mm = '0' + str_mm
        if len(str_hh) == 1:
            str_hh = '0' + str_hh
        if target in str_hh or target in str_mm :
            answer += 1
        start_total += 1
    return answer
 
 
start_hh, start_mm = map(int, input().split())
start_total = start_hh*60+ start_mm
end_hh, end_mm = map(int, input().split())
end_total = end_hh*60+ end_mm
target = input()
 
print(sol(start_total, end_total, target))
    