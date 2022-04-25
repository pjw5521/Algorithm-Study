import heapq

# 시간 분으로 바꾸기 
def time_to_min(s):
    s = s.split(':')
    
    hour = int(s[0]) * 60
    minute = int(s[1]) 
    
    return hour + minute 
   
# 분을 출력 형식에 맞는 시간으로 바꾸기  
def min_to_time(t):
    hour = str(t // 60)
    minute = str(t % 60)
    
    return hour.zfill(2) + ":" + minute.zfill(2)

def solution(n, t, m, timetable):
    answer = 0 
    arrive = []
    
    # 도착하는 시간 기준으로 최소 힙 구현 
    for i in timetable:
        heapq.heappush(arrive, time_to_min(i))

    # 버스 시작 시간 
    start = time_to_min('09:00')
    
    for _ in range(n) :
        # 셔틀에 타는 승객 수 
        cnt = 0 
        # 마지막 탑승한 승객의 도착 시간 
        last_t = 0 
        
        while arrive :
            # 셔틀보다 늦게 도착하면 중단 
            if arrive[0] > start :
                break 
            # 셔틀이 꽉 찼으면 중단 
            if cnt == m :
                break 
            # 승객 태우기 
            last_t = heapq.heappop(arrive)
            cnt += 1 
        
        # 셔틀에 아직 탈 수 있으면 
        if cnt < m :
            # 셔틀 도착시간 
            answer = start 
        # 셔틀이 꽉 찼으면 
        else :
            # 마지막으로 탑승한 승객보다 1분 빨리 와야 탈 수 있음 
            answer = last_t - 1 
        # 다음 셔틀 시간 갱신 
        start += t
        
    return min_to_time(answer)

n = 10
t = 60
m = 45
table = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
print(solution(n,t,m,table))