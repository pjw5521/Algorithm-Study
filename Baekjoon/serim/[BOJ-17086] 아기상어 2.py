from collections import deque


def bfs():
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < m:
                if count[a][b] == 0:
                    # 이동횟수 증가
                    count[a][b] = count[x][y] + 1
                    queue.append((a, b))


n, m = map(int, input().split())
count = []
queue = deque()
distance = 0

for i in range(n):
    graph = list(map(int, input().split()))
    for j in range(m):
        if graph[j] == 1:
            queue.append((i, j))
    count.append(graph)

bfs()

for i in range(n):
    for j in range(m):
        distance = max(distance, count[i][j])

print(distance - 1)