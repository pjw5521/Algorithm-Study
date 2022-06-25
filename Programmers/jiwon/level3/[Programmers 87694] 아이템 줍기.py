# https://programmers.co.kr/learn/courses/30/lessons/87694
from collections import deque 

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(board, cx,cy,ix,iy):
    q = deque()
    # 현재 위치, 이동 횟수 
    q.append((cx,cy,0))
    
    visited = [ [0] * 101 for _ in range(101)]
    visited[cx][cy] = True 
    
    while q :
        x ,y, cnt = q.popleft() 
        
        # 아이템 위치이면
        if x == ix and y == iy :
        	# 두배로 늘렸으므로, 2로 나눈 값 
            return cnt // 2 
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
        	# 범위에 속하고, 이동 가능한 위치이고, 방문하지 않았으면 
            if 0 <= nx < 101 and 0 <= ny < 101 and board[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx,ny,cnt+1))
                visited[nx][ny] = True 
                
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    board = [ [0] * 101 for _ in range(101)]

	# 네모 테두리, 내부 모두 1 로 표시 
    for x1, y1, x2, y2 in rectangle :
        for i in range(x1*2 , x2*2+1):
            for j in range(y1*2, y2*2+1):
                board[i][j] = 1 
                
    # 네모 내부는 0으로 표시하여, 테두리만 1로 표시되도록 
    for x1, y1, x2, y2 in rectangle :
        for i in range(x1*2+1 , x2*2):
            for j in range(y1*2+1, y2*2):
                board[i][j] = 0 
    
    # 현재 위치, 아이템 위치 두배 늘리기 
    cx, cy = characterX*2, characterY * 2 
    ix, iy = itemX *2 , itemY *2 
    
    return bfs(board, cx,cy,ix,iy)

r = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
cx = 1
cy = 3
ix = 7
iy = 8
print(solution(r,cx,cy,ix,iy))