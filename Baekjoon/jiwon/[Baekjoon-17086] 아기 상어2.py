# https://www.acmicpc.net/problem/17086
import sys
from collections import deque 

# 8방향 
nx = [1,-1,0,0, 1, 1, -1 ,-1]
ny = [0,0,1,-1,1,-1,-1,1]

def bfs(i,j):
    q = deque()
    
    # 방문 표시 
    visited = [[False] * m for _ in range(n)]
    visited[i][j] = True
    
    q.append((i,j,0))
    
    while q :
        x, y, cnt = q.popleft()
            
        # 아기상어를 만났으면 
        if graph[x][y] == 1 :
            return cnt 
            
        for i in range(8):
            dx = x + nx[i]
            dy = y + ny[i]
    
            if 0<=dx<n and 0<=dy< m and not visited[dx][dy]:
                q.append((dx,dy, cnt+ 1))
                visited[dx][dy] = True
                
input = sys.stdin.readline 

n, m = map(int,input().split())

graph = [] 
for _ in range(n) :
    graph.append(list(map(int,input().split())))
    
answer = 0
for i in range(n):
    for j in range(m):
        # 가장 가까운 아기상어 거리 중 최댓값 구하기
        if graph[i][j] != 1 :
            answer = max(answer,bfs(i,j))
            
print(answer)