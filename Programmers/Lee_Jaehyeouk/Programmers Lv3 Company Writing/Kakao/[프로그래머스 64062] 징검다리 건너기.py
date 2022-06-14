# 실패코드

def solution2(stones, k):
    answer = 0
    while(True):
        answer += 1
        for i in range(len(stones)):
            if stones[i] == 0:
                continue
            else:
                stones[i] -= 1
        count = 0
        for stone in stones:
            if stone == 0:
                count += 1
                if count == k:
                    return answer
            else:
                count = 0

# 효율성 참고 코드
def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        temp = stones.copy()
        # 이분 탐색
        mid = (left + right) // 2
        cnt = 0

        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

print(solution(stones,k))




