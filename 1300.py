from heapq import heapify, heappop

# 여전히 런타임 에러가 뜬다...
N = int(input())
k = int(input())
heap = []

for i in range(1,N+1):
    for j in range(1,N+1):
        heap.append(i*j)

heapify(heap)

for _ in range(k):
    ans = heappop(heap)

print(ans)