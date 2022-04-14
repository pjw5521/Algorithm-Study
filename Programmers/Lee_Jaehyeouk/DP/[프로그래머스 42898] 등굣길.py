# 이 문제의 핵심은 puddles 가 내가 생각하는 행과 열의 반대라는 것
# 두번째 고등학교때 방식으로 풀면 안되는게 [0,1], [1,0] 이 웅덩이 일 경우 생각해야 함


# 실패한 경우
def solution(m, n, puddles):

    maps = [[0 for _ in range(m)] for _ in range(n)]
    # 행렬 만들기 m = 열 n = 행
    for i in range(len(puddles)):
        maps[puddles[i][1]-1][puddles[i][0]-1] = 0
    maps[0][0] = 1
    for i in range(1,n):
        for j in range(1,m):
            if i == 0 and j == 0:
                continue
            elif maps[i][j] ==0:
                continue
            else:
                maps[i][j] = maps[i][j-1] + maps[i-1][j]
    return maps[n-1][m-1] % 1000000007

def solution(m, n, puddles):

    maps = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:  # (1,1)은 1으로 초기화
                maps[1][1] = 1
            elif [j, i] not in puddles:  # 물웅덩이가 아닌경우
                maps[i][j] = maps[i - 1][j] + maps[i][j - 1]

    return maps[n][m] % 1000000007