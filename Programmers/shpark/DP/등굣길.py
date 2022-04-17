# 좌 상
dx = [0, -1]
dy = [-1, 0]

def solution(m, n, puddles):
    answer = 0
    maps = [[0] * m for i in range(n)]
    dp = [[0] * m for i in range(n)]

    # 웅덩이 체크
    for j, i in puddles:
        maps[i-1][j-1] = 1

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            # 맨 처음 칸에 1 넣어줌
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue

            # 웅덩이 건너 뜀
            if maps[i][j] == 1:
                continue

            # 현재칸 기준 왼쪽 위쪽칸 값 더해줌
            # dp[i-1][j] + dp[i][j-1]
            sum = 0
            for d in range(2):
                nx = i + dx[d]
                ny = j + dy[d]

                # 배열 범위 체크
                if nx not in range(n) or ny not in range(m):
                    continue

                # 현재칸 기준 왼쪽 위쪽칸 값 더해줌
                # dp[i-1][j] + dp[i][j-1]
                sum += dp[nx][ny]

            # 현재 칸에 값 넣어줌
            dp[i][j] = sum % 1000000007


    answer = dp[n-1][m-1]
    return answer


m = 4
n = 3
p = [[2,2]]
solution(m, n, p)