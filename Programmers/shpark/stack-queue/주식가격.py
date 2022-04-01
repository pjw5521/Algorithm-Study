from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)

    while q:
        time = 0
        price = q.popleft()

        for i in len(q):
            time += 1
            if q[i] < price:
                break
        answer.append(time)

    return answer
