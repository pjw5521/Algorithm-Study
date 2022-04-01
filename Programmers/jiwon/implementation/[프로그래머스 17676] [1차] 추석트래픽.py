def get_time(n):
    # 시간, 분, 초 모두 초 단위로 변경 
    hour = int(n[:2]) * 3600 
    minute = int(n[3:5]) * 60
    second = int(n[6:8])
    
    millisecond = int(n[9:])
    
    # millisecond 단위로 변경 
    return (hour+minute+second)*1000 + millisecond 
    
def solution(lines):
    answer = 0
    
    # 요청 별 시작 시간, 종료 시간 저장 
    start_time = []
    end_time = [] 
    
    for i in lines:
    	# 공백 기준으로 나누기 
        time = i.split()
        
        # 처리 시간을 millisecond 단위로 변경 
        duration = int(float(time[2][:-1]) * 1000)
        # 완료 시간 구하기 
        end = get_time(time[1])
        # 시작 시간 구하기 
        start = end - duration + 1 
        
        start_time.append(start)
        end_time.append(end)
        
    for i in range(len(lines)):
        cnt = 0 
        end = end_time[i]
        
		# 종료 시간 기준 오름차순으로 정렬되어 있으므로 자기 자신보다 뒤에 있는 요청들만 비교
        for j in range(i,len(lines)):
       		# 같은 1초에 포함되어 있으면 
            if end + 1000 > start_time[j] :
                cnt += 1   
        # 최대 처리 개수 갱신 
        answer = max(answer,cnt)
               
    return answer