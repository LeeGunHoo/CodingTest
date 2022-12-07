from heapq import heapify, heappop

N, K = map(int, input().split())

heap = list(map(int, input().split()))
heapify(heap)

for _ in range(K):
    ans = heappop(heap)

print(ans)