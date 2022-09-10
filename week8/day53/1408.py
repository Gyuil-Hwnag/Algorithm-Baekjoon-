import sys
input = sys.stdin.readline

sh, sm, ss = map(int, input().split(':'))
eh, em, es = map(int, input().split(':'))

t = eh*3600+em*60+es - (sh*3600+sm*60+ss)

if t < 0:
    t += 60*60*24

h = t//3600 
m = (t%3600)//60 
s = t%60

print("%02d:%02d:%02d" % (h,m,s))