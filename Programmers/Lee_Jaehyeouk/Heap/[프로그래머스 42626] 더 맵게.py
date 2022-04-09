import heapq

def solution(scoville, k):
    cnt = 0
    heapq.heapify(scoville)

    while scoville[0] < k:
        if len(scoville) == 1:
            if scoville[0] <k:
                return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + (2 * heapq.heappop(scoville)))
        cnt += 1
    return cnt