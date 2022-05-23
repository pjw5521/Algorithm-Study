answer = int(1e9)

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, board, DP, result, last_dir):
    global answer
    if answer < result:
        return

    if x == len(board) - 1 and y == len(board) - 1:
        if answer > result:
            answer = result

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        # 배열 범위 체크
        if nx not in range(len(board)) or ny not in range(len(board)):
            continue

        # 벽 체크
        if board[nx][ny] == 1:
            continue

        # 직선 코너 계산
        sum = 100
        if d != last_dir:
            sum += 500

        if DP[nx][ny] < result + sum:
            continue
        DP[nx][ny] = result + sum

        dfs(nx, ny, board, DP, result+sum, d)




def solution(board):
    x, y = 0, 0
    DP = [[int(1e9)] * len(board) for i in range(len(board))]
    dfs(x, y, board, DP, 0, 1)
    dfs(x, y, board, DP, 0, 2)
    return answer
