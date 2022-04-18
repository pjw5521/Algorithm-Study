import heapq


def solution(jobs):
    answer = 0
    min_heap = []
    last = -1
    now = 0
    count = 0
    length = len(jobs)

    while count < length:
        for job in jobs:
            if last < job[0] <= now:
                answer += (now - job[0])
                heapq.heappush(min_heap, job[1])
        if min_heap:
            answer += (len(min_heap) * min_heap[0])
            last = now
            now += heapq.heappop(min_heap)
            count += 1
        else:
            now += 1

    return answer // length
