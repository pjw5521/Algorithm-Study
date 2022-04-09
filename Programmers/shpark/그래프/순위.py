from collections import defaultdict

def solution(n, results):
    answer = 0
    win_graph = defaultdict(set)
    lose_graph = defaultdict(set)

    for winner, loser in results:
        win_graph[loser].add(winner)
        lose_graph[winner].add(loser)

    # 순위 결정
    for i in range(1, n + 1):
        # 나한테 진 사람은 나를 이긴 사람한테도 진 것
        # ex) 순위 랭크 : 나 > A, B > 나 -> B > A
        for winner in win_graph[i]:
            lose_graph[winner].update(lose_graph[i])
        # 나한테 이긴 사람은 나한테 진 사람한테도 이긴 것
        # ex) 순위 랭크 : A > 나, 나 > B -> A > B
        for loser in lose_graph[i]:
            win_graph[loser].update(win_graph[i])

    # 각 선수가 이기고 진 애들이 합쳐서 n-1이면 순위가 결정됬다고 판단
    for i in range(1, n + 1):
        if len(win_graph[i]) + len(lose_graph[i]) == n - 1:  # i한테 이기고 진 애들 합쳐서 n-1이면 순위가 결정된 것
            answer += 1

    return answer