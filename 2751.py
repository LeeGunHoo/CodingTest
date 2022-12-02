from heapq import heappush, heappop

n = int(input())
heap = []

for _ in range(n):
    heappush(heap, input())

for _ in range(n):
    print(heappop(heap))