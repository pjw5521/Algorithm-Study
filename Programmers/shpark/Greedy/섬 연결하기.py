def solution(n, costs):
    answer = 0
    # 비용기준으로 오름차순 정렬
    costs.sort(key = lambda x: x[2])

    # 방문 확인
    visited = [False] * n
    visited[costs[0][0]] = True

    # 모든 섬이 연결될 때 까지 반복
    while visited.count(True) != n:
        for cost in costs:
            # 두 섬이 연결되어 있으면 continue
            if visited[cost[0]] == True and visited[cost[1]] == True:
                continue
            # 두 섬 중 하나만 방문했을 때
            if visited[cost[0]] == True or visited[cost[1]] == True:
                visited[cost[0]] = True
                visited[cost[1]] = True
                answer += cost[2]
                break
    return answer