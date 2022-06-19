from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((coin[0][0], coin[0][1], coin[1][0], coin[1][1], 0))

    while q:
        x_coin1, y_coin1, x_coin2, y_coin2, cnt = q.popleft()

        if cnt >= 10:
            return -1

        for d in range(4):
            nx_coin1 = x_coin1 + dx[d]
            ny_coin1 = y_coin1 + dy[d]
            nx_coin2 = x_coin2 + dx[d]
            ny_coin2 = y_coin2 + dy[d]

            # 두 동전이 빠지지 않을 경우
            if nx_coin1 in range(N) and ny_coin1 in range(M) and nx_coin2 in range(N) and ny_coin2 in range(M):
                if maps[nx_coin1][ny_coin1] == "#":
                    nx_coin1 = x_coin1
                    ny_coin1 = y_coin1
                if maps[nx_coin2][ny_coin2] == "#":
                    nx_coin2 = x_coin2
                    ny_coin2 = y_coin2
                q.append((nx_coin1, ny_coin1, nx_coin2, ny_coin2, cnt + 1))
            # 동전이 하나만 빠질 경우
            elif nx_coin1 in range(N) and ny_coin1 in range(M):
                return cnt + 1
            elif nx_coin2 in range(N) and ny_coin2 in range(M):
                return cnt + 1
            # 두 동전이 빠질 경우
            else:
                continue

    return -1

N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(input()))


coin = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 'o':
            coin.append([i, j])
result = bfs()
print(result)