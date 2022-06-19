from collections import deque


def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        now = queue.popleft()
        if now == k:
            print(visited[now])
            temp = now
            for i in range(visited[now] + 1):
                result.append(temp)
                temp = routes[temp]
            print(' '.join(map(str, result[::-1])))
            return
        for next in (now - 1, now + 1, now * 2):
            if 0 <= next <= 100000 and visited[next] == 0:
                visited[next] = visited[now] + 1
                queue.append(next)
                routes[next] = now


n, k = map(int, input().split())
visited = [0] * 100001
routes = [0] * 100001
result = []
bfs()