# https://programmers.co.kr/learn/courses/30/lessons/72413
def solution(n, s, a, b, fares):
    INF = int(1e9)
    
    graph = [ [INF] * (n+1) for _ in range(n+1)]
    
    for x, y, c in fares:
        graph[x][y] = c
        graph[y][x] = c 
        
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                graph[i][j] = 0
                
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    result = INF        
    for i in range(1, n+1):
        result = min(result, graph[s][i] + graph[i][a] + graph[i][b])
    
    return result
    
n = 7
s = 3
a = 4
b = 1 
f = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
print(solution(n,s,a,b,f))
