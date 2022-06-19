from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 8가지 이동방향
d = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
q = deque()

def bfs():
    print(q)
    while q:
        qx, qy = q.popleft()

        for dx, dy in d:
            x = qx + dx
            y = qy + dy
            # 맵에서 벗어나는 경우
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            # 상어가 없는 지점 or 미탐색 지점인지 확인
            if not graph[x][y]:
                # 새로운 지점의 거리 정보 업데이트
                graph[x][y] = graph[qx][qy] + 1
                # 새로운 지점의 좌표를 큐에 삽입
                q.append((x, y))
        print(qx,qy,graph)

# 상어의 위치에서부터 탐색 시작
for i in range(n):
    for j in range(m):
        # 상어 위치일 경우
        if graph[i][j]:
            # 상어 위치를 큐에 삽입
            q.append((i, j))

bfs()

# 정답 출력
print(max(map(max, graph)) - 1)
