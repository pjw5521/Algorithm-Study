# https://www.acmicpc.net/problem/1005
from collections import deque 
import sys 
input = sys.stdin.readline 

def topology_sort():
    q = deque()
    
    # 이전 건물의 최대 건설 소요 시간 저장 
    max_t = [0] * (n+1)
    
    # 진입 차수 0인 거 큐에 삽입 
    for i in range(1,n+1):
        if indegree[i] == 0 :
            q.append(i)
            
    while q :
        now = q.popleft()
            
        for i in graph[now] :
            # 해당 노드와 연결된 노드들의 진입차수 -1 
            indegree[i] -= 1 
            
            # 연결된 노드의 이전 건물 최대 건설 소요 시간이 현재 건물의 건설 시간보다 작다면 
            if max_t[i] < data[now]:
                # 최대 건설 소요 시간 갱신 
                max_t[i] = data[now]
                
            # 진입 차수 0이면 
            if indegree[i] == 0 :
                # 큐에 삽입하고 
                q.append(i)
                # 해당 건물까지 소요되는 건설 시간 갱신 
                data[i] = max_t[i] + data[i]
                
    return data[w]
    
test = int(input())

for _ in range(test):
    
    # 건물의 수, 건물 순서 규칙의 수
    n, k = map(int, input().split())
    
    # 걸리는 시간 
    data = [0]
    data.extend(list(map(int,input().split())))
    
    graph = [ [] for _ in range(n+1) ] 
    # 진입 차수 
    indegree = [0] * (n+1)
    for _ in range(k):
        a, b = map(int,input().split())
        graph[a].append(b)
        indegree[b] += 1 
    
    w = int(input())

    print(topology_sort())
        