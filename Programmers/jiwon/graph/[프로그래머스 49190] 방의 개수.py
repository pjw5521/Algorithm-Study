# https://programmers.co.kr/learn/courses/30/lessons/49190
from collections import defaultdict 

def solution(arrows):
    answer = 0
    # 경로 추가할 list 
    visited = defaultdict(list)
    
    # 번호에 따른 이동 방향 
    dx = [ -1, -1, 0, 1, 1, 1, 0, -1 ]
    dy = [ 0, 1, 1, 1, 0, -1, -1, -1 ]
    # 처음 위치 
    x,y = 0,0
    
    for arrow in arrows :
    	# 예외 case 해결을 위해 2칸 씩 검사해줘야 함 
        for _ in range(2):
            nx = x + dx[arrow]
            ny = y + dy[arrow]
            
            # 방문했던 정점이지만, 겹치는 경로가 아닌 경우
            if (nx,ny) in visited and (x,y) not in visited[(nx,ny)]:
            	# 방의 개수 + 1
                answer += 1 
                visited[(x,y)].append((nx,ny))
                visited[(nx,ny)].append((x,y))
            # 방문하지 않은 정점인 경우
            elif (nx,ny) not in visited:
                # 경로 추가 
                visited[(x,y)].append((nx,ny))
                visited[(nx,ny)].append((x,y))
            # 위치 갱신 
            x,y = nx,ny
            
    return answer
    
a = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
print(solution(a))