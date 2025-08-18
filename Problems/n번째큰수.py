import heapq

num = int(input())
heap = []
for _ in range(num):
    inputs = list(map(int, input().split()))
    for item in inputs:
        heapq.heappush(heap, item)

        if len(heap) > num: 
            heapq.heappop(heap)

print(heap)
popee = heapq.heappop(heap)
print(popee)
