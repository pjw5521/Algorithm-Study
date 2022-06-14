# 위상정렬
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # 건물의 개수 n, 건설 규칙 개수 k
    n, k = map(int, input().split())
    # 건물당 건설에 걸리는 시간 d
    d = list(map(int, input().split()))

    queue = deque()

    graph = [[] for _ in range(n + 1)]
    inDegree = [0 for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1

    # 최종 건설할 건물 번호
    w = int(input())

    for i in range(1, n + 1):
        if inDegree[i] == 0:
            queue.append(i)
            dp[i] = d[i - 1]

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            inDegree[i] -= 1
            # 더 오래 걸리는 시간을 넣어줌
            dp[i] = max(dp[i], dp[now] + d[i - 1])
            if inDegree[i] == 0:
                queue.append(i)

    print(dp[w])