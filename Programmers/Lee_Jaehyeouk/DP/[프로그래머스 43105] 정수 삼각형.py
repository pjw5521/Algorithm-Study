def solution(triangle):
    dp = []
    for i in range(1,len(triangle)+1):
        dp.append([0]*i)
    dp[0][0] = triangle[0][0]
    print(dp)

    for i in range(1,len(dp)):
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] = triangle[i][j] +dp[i-1][j]
            elif j == len(dp[i])-1:
                print(triangle[i][j])
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i-1][j-1],dp[i-1][j])
    return max(dp[-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution(triangle))




