def get_time(n):
    hour = int(n[:2]) * 3600 
    minute = int(n[3:5]) * 60
    second = int(n[6:8])
    millisecond = int(n[9:])
    
    return (hour+minute+second)*1000 + millisecond 
    
def solution(lines):
    answer = 0
    
    start_time = []
    end_time = [] 
    
    for i in lines:
        time = i.split()
        
        # 처리 시간 
        duration = int(float(time[2][:-1]) * 1000)
        end = get_time(time[1])
        start = end - duration + 1 
        start_time.append(start)
        end_time.append(end)
        
    for i in range(len(lines)):
        cnt = 0 
        end = end_time[i]

        for j in range(i,len(lines)):
            if end + 1000 > start_time[j] :
                cnt += 1   
        answer = max(answer,cnt)
               
    return answer