n = int(input())
a = []

# 일단 다 집어넣기
for i in range(n):
    a.append(input())

# 삽입 정렬 알고리즘 구현, 지원님 풀이 참고
for i in range(1, n):
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j-1], a[j] = a[j], a[j-1]
        else:
            break

for i in range(n):
    print(a[i])

