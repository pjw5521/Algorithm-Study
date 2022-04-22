def solution(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]]) # 집합
    while len(routes)!=n:
        for i, cost in enumerate(costs):
            print(routes, costs)
            if cost[0] in routes and cost[1] in routes: # 사이클 제외
                print("싸이클", i)
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break

    return ans

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

m = 5
costs2 = [[0,1,1],[0,4,10],[4,1,2],[1,2,5],[3,2,3],[3,4,1],[2,4,16]]
#print(solution(n,costs))
print(solution(m,costs2))