# 주의해야 할 점은 위치를 (m,n)으로 나타낸다는 것 
def solution(m, n, puddles):
    dp = [ [0] * m for _ in range(n) ]
    dp[0][0] = 1 
    
    # 물에 잠긴 지역 . 으로 표시 
    for x, y in puddles :
        # 좌표 위치 변경해줘야함 
        dp[y-1][x-1] = '.'
      
    # 가로 첫째줄은 오른쪽으로 이동하는 것만 가능   
    for i in range(1,m):
        # 물에 잠긴 지역이 있다면 그 지역 오른쪽 지역 모두 지나가지 못함 
        if dp[0][i] == '.' :
            break           
        dp[0][i] = dp[0][i-1]
    
    # 세로 첫째줄은 아래쪽으로 이동하는 것만 가능 
    for i in range(1,n):
        # 물에 잠긴 지역이 있다면 그 지역 아래쪽 지역 모두 지나가지 못함 
        if dp[i][0] == '.':
            break
        dp[i][0] = dp[i-1][0]
        
    for i in range(1,n):
        for j in range(1,m):
            # 물에 잠긴 지역이면 넘어감 
            if dp[i][j] == '.':
                continue 
            # 오른쪽으로 이동 
            if dp[i-1][j] != '.':
                dp[i][j] +=  dp[i-1][j]
            # 아래쪽으로 이동 
            if dp[i][j-1] != '.':
                dp[i][j] +=  dp[i][j-1]
   
    return (dp[n-1][m-1] %1000000007)