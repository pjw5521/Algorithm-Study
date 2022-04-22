from itertools import combinations


def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    rocks.sort()

    # 이분 탐색
    while start <= end:
        mid = (start + end) // 2  # 중간값을 구한다.
        del_stones = 0  # 제거한 돌을 카운트하기 위한 변수
        cur_stone = 0  # 시작지점
        for rock in rocks:
            if rock - cur_stone < mid:  # 돌사이의 거리가 가정한 값보다 작으면 제거한다.
                del_stones += 1
            else:  # 아니라면 그 돌을 새로운 기준으로 세운다.
                cur_stone = rock
            if del_stones > n:  # 제거된 돌이 문제 조건 보다 크면 for문을 나온다
                break
        if del_stones > n:  # 제거된 돌이 너무 많으면 가정한 값이 큰 것이므로 범위를 작은 쪽으로 줄인다.
            end = mid - 1
        else:  # 반대라면 큰 쪽으로 줄인다.
            answer = mid
            start = mid + 1

    return answer

distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2

print(solution(distance,rocks,n))