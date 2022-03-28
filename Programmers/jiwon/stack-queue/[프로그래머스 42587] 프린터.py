from collections import deque 

def solution(priorities, location):
    answer = 0
    q = deque()
    
    # 작업의 위치와 우선순위를 큐에 삽입 
    for i in range(len(priorities)):
        q.append((i, priorities[i]))
        
    # 우선순위 내림차순 정렬 
    priorities.sort(reverse = True)
    # 남은 인쇄 목록의 가장 높은 우선순위의 인덱스
    index = 0 
    # 인쇄 순서 
    cnt = 0
    
    while q :
        x, p = q.popleft()
        
        # 남은 인쇄 목록의 가장 큰 우선순위와 같다면, 인쇄 가능 
        if p == priorities[index]:
            # 인쇄할 작업의 위치가 찾고자 하는 위치이면 
            if x == location:
                # 인쇄 순서 +1 한 후 정답 리턴 
                cnt += 1 
                return cnt 
            # 순서를 찾고자 하는 작업이 아니면 
            else:
                # 우선순위 인덱스, 순서 + 1
                index += 1 
                cnt += 1 
                
        # 더 큰 우선순위가 남아있다면 맨 뒤에 추가 
        else:
            q.append((x,p))
