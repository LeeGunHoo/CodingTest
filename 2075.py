#1 메모리 초과
# from heapq import heapify, heappop, heappush
# n = int(input())
# l = []
# i = 1
#
# for _ in range(n):
#     num_list = map(int, input().split())
#     for num in num_list:
#         heappush(l, -num)
#
# while True:
#     if i == n:
#         ans = heappop(l)
#         break
#     else:
#         heappop(l)
#     i += 1
#
# print(-ans)

#2 개선 (12/5)
# 메모리 초과이므로 l의 공간복잡도가 너무 클 것으로 예상
# 줄여주려면 결국 작은건 쳐내야 한다.
from heapq import heapify, heappop, heappush
n = int(input())
l = []
i = 1

for _ in range(n):
    num_list = map(int, input().split())
    for num in num_list:
        # 작은거 쳐낼 수 있는 부분이 여기밖에 없다.
        if len(l) < n:
            heappush(l, -num)
        else:
            l[-1] = -num

while True:
    if i == n:
        ans = heappop(l)
        break
    else:
        heappop(l)
    i += 1

print(-ans)