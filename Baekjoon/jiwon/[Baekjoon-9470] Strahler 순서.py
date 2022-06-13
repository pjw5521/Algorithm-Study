# https://www.acmicpc.net/problem/9470
from collections import deque 

def topology_sort():
    q = deque()
    # 들어오는 최대 레벨, 최대 레벨의 개수 
    num = [[0,0]] * (m+1)
    
    # 진입 차수 0인 거 큐에 담기 
    for i in range(1,m+1):
        if indegree[i] == 0 :
            # 최대 레벨 1, 레벨 1인 노드의 개수 1개 
            num[i] = [1,1]
            q.append(i)
    
    # 순서 번호 저장할 배열
    order = [0] * (m+1)        
    while q :
        now = q.popleft()
        
        # 최대 레벨의 개수가 2개 이상이면 
        if num[now][1] >= 2 :
            # 최대 레벨 + 1 
            order[now] = num[now][0] + 1 
        # 아니면 최대 레벨과 동일 
        else :
            order[now] = num[now][0]

        for i in graph[now]:
            # 해당 노드와 연결된 노드들의 진입차수 -1 
            indegree[i] -= 1 
            # 최대 레벨 번호 같으면 개수 증가 
            if num[i][0] == order[now] :
                num[i][1] += 1 
            # 더 크면 갱신 
            elif num[i][0] < order[now] :
                num[i] = [order[now], 1]
            
            # 진입 차수 0 이면 큐에 삽입 
            if indegree[i] == 0 :
                q.append(i)
                
    # 노드 m의 순서 번호 리턴 
    return order[m]     
                  
test = int(input())

for _ in range(test):
    # 테스트 케이스 번호, 노드 수, 간선 수 
    k, m, p = map(int,input().split())
    
    # 모든 노드의 진입차수는 0으로 초기화
    indegree = [0] * (m+1)
    graph = [ [] for _ in range(m+1)]
    
    for _ in range(p):
        a, b = map(int,input().split())
        
        # a에서 b로 이동 가능 
        graph[a].append(b)
        # b의 진입차수 + 1 
        indegree[b] += 1
    
    print(k, end = " ")
    print(topology_sort())