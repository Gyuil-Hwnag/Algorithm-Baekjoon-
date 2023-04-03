## 14584
import sys

def calc(key, n, words):
    for i in range(26):
        temp = ""
        for k in key:
            temp += chr(((ord(k)-97+i)%26)+97)

        for k in range(n):
            if words[k] in temp:
                return temp

key = sys.stdin.readline()[:-1]
n = int(sys.stdin.readline())
words = []
for _ in range(n):
    word = input()
    words.append(word)

print(calc(key, n, words))