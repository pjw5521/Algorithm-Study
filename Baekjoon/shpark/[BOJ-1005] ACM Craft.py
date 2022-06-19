from collections import defaultdict, deque

def run():
    DP = [0] * (N+1)
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            DP[i] += Delay[i]

    while q:
        now = q.popleft()

        for i in dict[now]:
            indegree[i] -= 1
            DP[i] = max(DP[i], DP[now] + Delay[i])

            if indegree[i] == 0:
                q.append(i)

    return DP[W]

T = int(input())
for test_case in range(T):
    # N : 건물의 개수, K : 규칙의 총 개수
    N, K = map(int, input().split())
    # 건설에 걸리는 시간
    Delay = [0] + list(map(int, input().split()))
    dict = defaultdict(list)
    indegree = [0] * (N + 1)
    for i in range(K):
        A, B = map(int, input().split())
        dict[A].append(B)
        indegree[B] += 1

    # 도착할 건물의 번호
    W = int(input())

    result = run()
    print(result)