# 같은 단어는 한 번만 출력이기에 set으로 받는다.
n = int(input())
word = set()

# 단어를 n개 만큼 받아본다.
for _ in range(n):
    word.add(input())

# 정렬하기 위해 list로 바꿔주자.
word = list(word)

# 길이 순으로 정렬해야하는데, 길이 2짜리 튜플 넣으면 어짜피 앞에 요소가 우선적으로 배열됨
len_word = []
for w in word:
    len_word.append((len(w), w))

sort_len_word = sorted(len_word)

for length, w in sort_len_word:
    print(w)
