from collections import deque

def bfs(start, end):
    q = deque()
    # start, cnt
    q.append([start, 0])
    visited[start] = start

    while q:
        x, cnt = q.popleft()

        # 동생 발견
        if x == end:
            return cnt

        cnt += 1
        for i in range(3):
            if i == 0:
                nx = 2 * x
            elif i == 1:
                nx = x + 1
            else:
                nx = x - 1

            if nx not in range(0, 100001):
                continue
            if visited[nx] != 0:
                continue

            q.append([nx, cnt])
            visited[nx] = x


N, K = map(int, input().split())
visited = [0] * 100001
result = []
cnt = bfs(N, K)

# 역순으로 경로 저장
temp = K
for i in range(cnt):
    result.append(temp)
    temp = visited[temp]
result.append(N)

# 결과 출력
print(cnt)
print(*result[::-1])
