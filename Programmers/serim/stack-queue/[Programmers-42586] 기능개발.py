from collections import deque
import math


def solution(progresses, speeds):
    result = []
    queue = deque()
    num = 1

    # queue에 작업 일수 넣어주기
    for i in range(len(progresses)):
        queue.append(math.ceil((100 - progresses[i]) / speeds[i]))

    # 가장 먼저 시작하는 일의 작업 기간
    first = queue.popleft()

    while queue:
        now = queue.popleft()
        # 먼저 시작된 작업의 기간보다 현재 작업 기간이 짧을 경우
        if first >= now:
            # 먼저 시작된 작업과 함께 끝나므로 count 1 추가
            num += 1
        # 먼저 시작된 작업의 기간보다 현재 작업 기간이 길 경우
        else:
            # 먼저 시작되었으며 함께 종료될 작업들의 개수를 결과 리스트에 추가
            result.append(num)
            # 작업의 개수 1로 초기화
            num = 1
            # 현재 작업이 가장 먼저 시작된 긴 작업이 됨
            first = now
    # 마지막 작업에 대해서도 결과에 포함해야 함
    result.append(num)

    return result
