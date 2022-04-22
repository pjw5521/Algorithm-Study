# Kruskal 알고리즘: Greedy를 이용하여 네트워크의 모든 정점을 최소 비용으로 연결하는 최적 해답을 구하는것
# https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html

def solution(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]]) # 집합
    print(costs)
    print(routes)
    while len(routes)!=n:
        for i, cost in enumerate(costs):
            print(i,cost)
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return ans

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n,costs))