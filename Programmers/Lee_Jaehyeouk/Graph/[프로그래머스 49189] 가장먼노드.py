from collections import deque

n = 6
v = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def bfs(v, distance, node):
    cnt = 0
    q = deque([[v, cnt]])
    print(q)
    while q:
        val = q.popleft()
        v = val[0] # 시작 노드
        cnt = val[1] # 카운트 세기 시작
        if distance[v] == -1:
            distance[v] = cnt
            cnt += 1
            for e in node[v]:
                q.append([e,cnt])
        print(q)

def solution(n,edge):
    answer = 0
    distance = [-1] * (n+1)
    node = [[] for _ in range(n+1)]
    for e in edge:
        x = e[0]
        y = e[1]
        node[x].append(y)
        node[y].append(x)
    #print(node)
    bfs(1,distance,node)
    #print(distance)
    #print(node)
    for value in distance:
        if value == max(distance):
            answer = answer+1
    return answer

solution(n,v)
