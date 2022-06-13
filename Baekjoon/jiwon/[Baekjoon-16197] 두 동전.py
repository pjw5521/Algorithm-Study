# https://www.acmicpc.net/problem/16197
from collections import deque
import sys
input= sys.stdin.readline 

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x1,y1, x2, y2):
    q = deque()
    q.append((x1,y1,x2,y2, 0))
    
    while q :
        x1, y1, x2, y2, cnt = q.popleft()
            
        # 10번보다 많이 이동해야하면 -1 리턴 
        if cnt >= 10 :
            return -1 
            
        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]     
                
            # 둘 중에 하나만 떨어지면    
            if (not( 0<=nx1<n and 0<=ny1<m) and (0<=nx2<n and 0<=ny2<m)) or (not( 0<=nx2<n and 0<=ny2<m) and (0<=nx1<n and 0<=ny1<m)):
                return cnt + 1
            
            # 움직일 수 있으면 
            if (0<=nx1<n and 0<=ny1<m) and (0<=nx2<n and 0<=ny2<m):
                # 벽이면 움직이지 못함 
                if graph[nx1][ny1] == '#':
                    nx1 = x1
                    ny1 = y1
                if  graph[nx2][ny2] == '#':
                    nx2 = x2
                    ny2 = y2
                
                q.append((nx1,ny1,nx2,ny2, cnt +1))
            # 둘 다 범위를 벗어나면 
            else :
                continue 
                
    return -1 
                    
n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(str,input())))

coin = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'o':
            coin.append((i,j))
            
answer = bfs(coin[0][0], coin[0][1], coin[1][0], coin[1][1])
print(answer)