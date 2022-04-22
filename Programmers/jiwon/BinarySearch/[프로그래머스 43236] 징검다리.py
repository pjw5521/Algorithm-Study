def solution(distance, rocks, n):
    answer = 0
    # 이분 탐색 시작 범위 설정 
    start = 0
    end = distance
    # 시작위치에서 바위까지 거리 오름차순 정렬 
    rocks.sort()
    # 도착 지점 추가 
    rocks.append(distance)
    
    while start <= end :
        # 최소 거리 
        mid = (start+end) // 2 
        # 제거한 바위 개수
        cnt = 0 
        # 시작 위치 
        now = 0 
        
        for i in rocks :
            # 현재 위치에서 바위까지 거리
            dist = i - now 
            # 최소거리보다 작으면 
            if dist < mid :
                # 바위 제거 
                cnt +=1 
            else :
                # 최소거리와 크거나 같으면 그 바위로 이동 
                now = i
         
        # 바위가 n보다 많이 제거됐으면 최소 거리 줄이기        
        if cnt > n :
            end = mid - 1 
        else :
        	# 최소 거리 늘리기 
            answer = mid 
            start = mid + 1 
            
    return answer
    
dist = 25
rock = [2, 14, 11, 21, 17]
n = 2
print(solution(dist,rock,n))