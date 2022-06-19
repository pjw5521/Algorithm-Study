from collections import deque


def bfs():
    queue = deque()
    queue.append((a, 1))
    while queue:
        now, result = queue.popleft()
        if now > b:
            continue
        if now == b:
            print(result)
            break
        if int(str(now) + '1') <= b:
            queue.append((int(str(now) + '1'), result + 1))
        if now * 2 <= b:
            queue.append((now * 2, result + 1))
    else:
        print(-1)


a, b = map(int, input().split())
bfs()