import heapq

N = int(input())
hq = []
for _ in range(N):
    lst = list(map(int, input().split()))
    print(lst)
    # 힙이 비어있으면,
    if not hq:
        for tmp in lst:
            # 힙정렬해서 값 넣기
            heapq.heappush(hq, tmp)

    # 두번째 열부터
    else:
        for tmp in lst:
            # 젤 작은값보다 큰 값이 있으면,
            if hq[0] < tmp:
                heapq.heappush(hq, tmp)
                heapq.heappop(hq)
print(hq[0])