from collections import deque 

def bfs():
    
    q = deque()
    # visited[화면 개수][클립보드 개수] 방문 표시 
    visited = [ [0] * (s+1) for _ in range(s+1) ] 
    visited[1][0] = True
    # (화면개수, 클립보드개수, 연산횟수 )
    q.append((1,0,0))
    
    while q :
        screen, board, cnt = q.popleft()
        
        # 화면에 있는 이모티콘 개수가 s개 이면 연산횟수 리턴 
        if screen == s :
            return cnt 
            
        # 클립보드에 저장 
        if not visited[screen][screen] :
            q.append((screen,screen, cnt+1))
            visited[screen][screen] = True
            
        # 화면에 붙여넣기 
        if screen + board < s+1 :
            if not visited[screen + board][board] :
                q.append((screen +board, board, cnt + 1))
                visited[screen+board][board] = True 
        
        # 화면의 이모티콘 하나 삭제하기 
        if screen -1 >= 0:
            if not visited[screen-1][board] :
                q.append((screen-1, board ,cnt +1))
                visited[screen-1][board] = True       
                
    return -1  
        
s = int(input())
print(bfs())