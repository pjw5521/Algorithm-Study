#틀린 코드
def solution(n):
    answer = 0
    dp = [1,2]
    for i in range(2,n):
        x = dp[i-1]+dp[i-2]
        dp.append(x)
    answer = dp[-1]%1000000007
    return answer

#맞은 코드
def solution(n):
    answer = 0
    dp = [1,2]
    for i in range(2,n):
        x = (dp[i-1]+dp[i-2])%1000000007
        dp.append(x)
    answer = dp[-1]
    return answer

print(solution(4))

