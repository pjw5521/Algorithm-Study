# https://programmers.co.kr/learn/courses/30/lessons/42861

# 크루스칼 알고리즘 
def solution(n, costs):
    # cost 기준으로 오름차순 정렬 
    costs.sort(key = lambda x : x[2])
    
    # 첫 출발지와 도착지
    connect = set([costs[0][0], costs[0][1]])
    # 첫 가중치
    answer = costs[0][2]
    
    while len(connect) < n:
        for cost in costs:
            # 출발지와 목적지 모두 connect에 존재하면 넘어감 
            if cost[0] in connect and cost[1] in connect :
                continue 
            # 두 섬 중 하나만 connec에 있는 경우 
            if cost[0] in connect or cost[1] in connect :
                # 출발지와 목적지 추가 
                connect.update([cost[0],cost[1]])
                # 가중치 더하기 
                answer += cost[2]
                break 
            
    return answer
  
n = 5
c = [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]	
print(solution(n,c))
  
''' 원래 접근 방법 : 다익스트라 / 그러나 본 문제는 가장 빠른 길을 선택하는 것이 아님
from collections import deque 
import heapq 
INF = int(1e9)

def dijkstra(graph, start,n):
    q = []
    heapq.heappush(q,(0,start))
    distance = [INF] * (n)
    path = [ [] for _ in range(n)]
    path[start].append(start)
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist :
            continue 
    
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]] :
                distance[i[0]] = cost 
                path[i[0]] =[]
                for k in path[now]:
                    path[i[0]].append(k)
                path[i[0]].append(i[0])
                heapq.heappush(q, (cost, i[0]))
    
    answer = INF
    
    for i in range(n):
        if len(path[i]) == n :
            answer= min(answer, distance[i])

    return answer 
            
def solution(n, costs):
    answer = INF
    graph = [ [] for _ in range(n) ]

    for a, b, c in costs:
        graph[a].append((b,c))
        graph[b].append((a,c))
        
    for i in range(n):
        answer = min(answer, dijkstra(graph, i, n))
        
    return answer

'''
