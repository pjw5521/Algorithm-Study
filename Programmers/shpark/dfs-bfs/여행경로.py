from collections import defaultdict

answer = []


def dfs(start, cnt, arr, N, maps, visited):
    global answer

    # 모든 항공권 사용
    if cnt == N:
        answer = arr
        return

    # 모든 항공권을 사용 했을 때
    if len(answer) >= 1:
        return

    for i in range(len(maps[start])):
        if visited[start][i] == 0:
            visited[start][i] = 1
            dfs(maps[start][i], cnt + 1, arr + [maps[start][i]], N, maps, visited)
            visited[start][i] = 0


def solution(tickets):
    maps = defaultdict(list)
    visited = defaultdict(list)

    # dict에 넣기
    for i in range(len(tickets)):
        start = tickets[i][0]
        end = tickets[i][1]
        maps[start].append(end)
        visited[start].append(0)

    # 정렬 (경로가 여러 개 일 때, 알파벳 순서가 앞서는 경로부터 넣기 위해)
    for i in maps.keys():
        maps[i].sort()

    start = tickets[0][0]
    arr = [start]
    N = len(tickets)
    dfs("ICN", 0, ["ICN"], len(tickets), maps, visited)

    return answer