from collections import deque

# 8방향
# 좌상, 상, 우상, 우, 우하, 하, 좌하, 좌
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def bfs(x, y):
    q = deque()
    q.append([x, y, 0])
    visited = [[0] * M for i in range(N)]
    visited[x][y] = 1

    while q:
        x, y, cnt = q.popleft()

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            # 배열 범위 체크
            if nx not in range(N) or ny not in range(M):
                continue
            # 방문 체크
            if visited[nx][ny] == 1:
                continue

            if maps[nx][ny] == 1:
                return cnt + 1

            q.append([nx, ny, cnt+1])
            visited[nx][ny] = 1


N, M = map(int ,input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

answer = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            result = bfs(i, j)
            answer.append(result)

print(max(answer))