#72ms
words = input()
alp = [0 for _ in range(26)]
odd_cnt = 0
odd_word = ''
res = ''

for word in words:
    alp[ord(word) - 65] += 1

for i in range(len(alp)):
    if alp[i] % 2 == 1:
        odd_cnt += 1
        odd_word += chr(i + 65)
    res += chr(i+65) * (alp[i] // 2)

if odd_cnt > 1:
    print("I'm Sorry Hansoo")
else:
    print(res + odd_word + res[::-1])

#92ms
from collections import Counter

words = input()
cnt = Counter(words)
odd_cnt = 0
odd_word = ''
res = ''

for i in range(26):
    alp = chr(i+65)
    if cnt[alp] % 2 == 1:
        odd_cnt += 1
        odd_word += chr(i + 65)
    res += chr(i+65) * (cnt[alp] // 2)

if odd_cnt > 1:
    print("I'm Sorry Hansoo")
else:
    print(res + odd_word + res[::-1])

# https: // alpyrithm.tistory.com / 100