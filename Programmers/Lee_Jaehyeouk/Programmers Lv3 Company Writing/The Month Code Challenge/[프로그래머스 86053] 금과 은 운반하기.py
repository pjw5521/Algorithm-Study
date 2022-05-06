# 이분 탐색을 이용해서 풀이
# 최악의 시간을 가정 해서 해당 시간 동안 가져올 수 있는 최대의 광물 계산
# 계산 된 광물과 answer 을 비교 진행
# 값이 더 작은 쪽을 answer 로 하고 다시 진행

def solution(a, b, g, s, w, t):
    start = 0
    end = (10 ** 9) * (10 ** 5) * 4
    answer = (10 ** 9) * (10 ** 5) * 4

    while start <= end:
        mid = (start + end) // 2
        current_gold = 0
        current_silver = 0
        total = 0
        print(answer, mid)

        for i, time in enumerate(t):
            cnt = (mid - time) // (time * 2) + 1

            if cnt * w[i] > g[i]:
                current_gold += g[i]
            if cnt * w[i] <= g[i]:
                current_gold += cnt * w[i]
            if cnt * w[i] > s[i]:
                current_silver += s[i]
            if cnt * w[i] <= s[i]:
                current_silver += cnt * w[i]
            if s[i] + g[i] < cnt * w[i]:
                total += s[i] + g[i]
            if s[i] + g[i] >= cnt * w[i]:
                total += cnt * w[i]
        if current_gold >= a and current_silver >= b and total >= a + b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1

    return (answer)

print(solution(10,10,[100],[100],[7],[10]))

#print(solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1]))









