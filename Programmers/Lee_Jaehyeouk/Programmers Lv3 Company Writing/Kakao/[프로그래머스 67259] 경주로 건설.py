
from collections import deque

def solution(board):
    dx = [0, 1, -1, 0]
    dy = [-1, 0, 0, 1]
    inf = 1e9

    N = len(board)
    arr = [[[inf] * 4 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append([0, 0, -1])
    arr[0][0] = [0, 0, 0, 0]

    while queue:
        x, y, direction = queue.popleft()
        print(x, y,direction, arr)
        for i in range(4):
            if i + direction == 3:
                continue
            nx = x + dx[i]
            ny = y + dy[i]
            cost = 100
            if i != direction and direction != -1:
                cost += 500
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1 and arr[nx][ny][i] > cost + arr[x][y][direction]:
                arr[nx][ny][i] = cost + arr[x][y][direction]
                queue.append([nx, ny, i])


    return min(arr[N - 1][N - 1])

board = [[0,0,0],[0,0,0],[0,0,0]]

board1 = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]

board2 = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]

board3 = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]

print(solution(board))