# https://programmers.co.kr/learn/courses/30/lessons/64062
def solution(stones, k):
    answer = 0
    
    start = 1
    end = max(stones)
    
    while start <= end :
        # 건널 수 있는 최대 사람 수 
        mid = (start + end) // 2 
        cnt = 0 
        
        for s in stones :
            # 건너뛰어야 하는 디딤돌
            if s - mid <= 0 :
                cnt += 1               
            else :
                cnt = 0 
            
            if cnt >= k :
                break 
        
        # 건널 수 있는 최대 칸 수보다 많으면 사람 수 줄이기 
        if cnt >= k :
            answer = mid 
            end = mid - 1 
        # 사람 수 늘리기 
        else :
            start = mid + 1

    return answer
    
s = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3 
print(solution(s,k))