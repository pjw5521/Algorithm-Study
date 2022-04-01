from collections import deque

def bfs(v, visited, node):
    cnt = 0
    q = deque([[v, cnt]])
    while q:
        val = q.popleft()
        v = val[0]
        cnt = val[1]
        if visited[v] == -1:
            visited[v] = cnt
            cnt += 1
            for e in node[v]:
                q.append([e,cnt])

def solution(n,edge):
    answer = 0
    visited = [-1] * (n+1)
    node = [[] for _ in range(n+1)]
    for e in edge:
        x = e[0]
        y = e[1]
        node[x].append(y)
        node[y].append(x)
    bfs(1,visited,node)
    for value in visited:
        if value == max(visited):
            answer = answer+1
    return answer

