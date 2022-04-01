from collections import deque

def bfs(v, distance, node):
    cnt = 0
    q = deque([[v, cnt]])
    while q:
        val = q.popleft()
        v = val[0]
        cnt = val[1]
        if distance[v] == -1:
            distance[v] = cnt
            cnt += 1
            for e in node[v]:
                q.append([e,cnt])
#

def solution(n,edge):
    answer = 0
    distance = [-1] * (n+1)
    node = [[] for _ in range(n+1)]
    for e in edge:
        x = e[0]
        y = e[1]
        node[x].append(y)
        node[y].append(x)
    bfs(1,distance,node)
    print(distance)
    print(node)
    for value in distance:
        if value == max(distance):
            answer = answer+1
    return answer

solution(n,v)
