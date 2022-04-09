def solution(n, times):
    answer = 0
    # 걸릴 시간 최대값을 right에 넣음
    left, right = 1, max(times) * n
    while 1:
        # 이분탐색 탈출조건
        if left > right:
            break
        mid = (left + right) // 2

        # 심사한 사람 수
        people = 0
        for time in times:
            people = people + (mid // time)

            # 심사한 사람 수가 많으면 탈출
            if people >= n:
                break

        # 심사한 사람 수가 많으면
        if people >= n:
            answer = mid
            right = mid - 1
        # 심사한 사람 수가 적으면
        elif people < n:
            left = mid + 1
    return answer

a = 6
b = [7, 10]

solution(a,b)