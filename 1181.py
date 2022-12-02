# 같은 단어는 한 번만 출력이기에 set으로 받는다.
n = int(input())
word = set()

# 단어를 n개 만큼 받아본다.
for _ in range(n):
    word.add(input())

# 정렬하기 위해 list로 바꿔주자.
word = list(word)

len_word = []
for i in word:
    len_word.append(len(i))
