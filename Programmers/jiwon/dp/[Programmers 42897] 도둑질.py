def solution(money):
    answer = 0
    n = len(money)
    
    # dp[i]는 i번째 집까지 털 수 있는 최대 금액 
    dp = [0] * n
   
    # 첫번째 집 털고, 마지막 집을 털지 않을 경우 
    dp[0] = money[0]
    dp[1] = max(money[1], money[0])
   
    # 마지막 집은 확인 x 
    for i in range(2,n-1):
        dp[i] = max(dp[i-1], dp[i-2]+ money[i])
    
    # 마지막 집을 털지 않았으므로 
    result = dp[n-2]
    
    # 첫번째 집을 털지 않고, 마지막 집을 털 경우 
    # dp 초기화 
    dp = [0] * n
    dp[0] = 0 
    dp[1] = money[1]
    
    for i in range(2,n):
        dp[i] = max(dp[i-1], dp[i-2]+ money[i])
    
    # 최댓값 
    result = max(result, dp[n-1])
    
    return result
    
m = [1, 2, 3, 1]
print(solution(m))