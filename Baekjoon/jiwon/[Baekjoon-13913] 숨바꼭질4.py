from collections import deque 
import sys
input = sys.stdin.readline 

def bfs(n,k):
    
    q = deque()
    # 방문표시 
    visited = [False] * 100001
    visited[n] = True
    # 자취를 저장할 배열 
    path =[0] * 100001
    # 출발지 표시 
    path[n] = n
    # 위치, 이동 횟수 
    q.append((n,0))

    while q:
        now, cnt = q.popleft()
    
   		# k에 도착했다면 
        if now == k :
            print(cnt)
     		# 경로를 기록할 배열 
            answer = []
            x = now
            answer.append(x)
            # 출발지에 도착하기 전까지 
            while path[x] != x :
            	# 경로 읽기 
                answer.append(path[x])
                x = path[x]
            # 거꾸로 저장되어있으므로 
            answer.reverse()
            # 출력 
            print(*answer)
            return answer 
            
        # 범위에 속하고 방문하지 않았으면 
        if now + 1 < 100001 and not visited[now+1] :
        	#자취 표시
            path[now+1] = now
            # 큐에 삽입 
            q.append((now+1, cnt +1 ))
            # 방문 표시 
            visited[now+1] = True
            
        # 범위에 속하고 방문하지 않았으면 
        if 0 <= now - 1 < 100001 and not visited[now-1]:
            path[now-1] = now
            q.append((now-1, cnt +1))
            visited[now-1] = True
        
        # 범위에 속하고 방문하지 않았으면     
        if now * 2 < 100001  and not visited[now*2] :
            path[now*2] = now 
            q.append((now*2, cnt +1))
            visited[now*2] = True
            
    return -1 
    
n, k = map(int,input().split())
bfs(n,k)