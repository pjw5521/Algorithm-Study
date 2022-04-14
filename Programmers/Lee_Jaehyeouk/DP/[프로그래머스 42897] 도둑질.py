# 풀이 방법
# 이게 결국 첫번재 집과 두번째 집을

def solution(money):
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)
    # 1번 집을 터는 경우
    dp1[0] = money[0]
    for i in range(1, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
        print(dp1)
    dp1[0] = 0
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
    return max(dp1[-2], dp2[-1])

l = [1,3,10,1,1,0,60]
print(solution(l))
