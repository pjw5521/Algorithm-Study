def solution(n, s, a, b, fares):
    answer = 1e9
    dist = [[1e9] * (n + 1) for _ in range(n + 1)]
    for i, j, cost in fares:
        dist[i][j] = dist[j][i] = cost

    for i in range(1, n + 1):
        dist[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    for i in range(1, n + 1):
        cost = dist[s][i] + dist[i][a] + dist[i][b]
        answer = min(answer, cost)

    return answer