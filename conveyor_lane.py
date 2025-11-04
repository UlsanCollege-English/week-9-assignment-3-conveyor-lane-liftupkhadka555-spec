import heapq

def sort_k_sorted(arr, k):
    if not arr:
        return []

    n = len(arr)
    result = []
    heap = []

    for i in range(min(k, n)):
        heapq.heappush(heap, arr[i])

    for i in range(k, n):
        heapq.heappush(heap, arr[i])
        result.append(heapq.heappop(heap))

    while heap:
        result.append(heapq.heappop(heap))


    result.sort()
    return result
