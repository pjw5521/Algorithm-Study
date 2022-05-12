# https://programmers.co.kr/learn/courses/30/lessons/72414

# 초단위로 변경하는 함수 
def time_cal(t):
    h, m, s = t.split(":")
    
    h = int(h) * 3600
    m = int(m) * 60 
    s = int(s)
    
    return h+m+s
    
# 초 단위로 표현된 시간을 출력 형식에 맞게 변경하는 함수 
def str_cal(t):
    h = str(t // 3600)
    t = t % 3600 
    
    m = str(t // 60)
    t = t % 60
    
    s = str(t)
    
    return h.zfill(2) + ":" + m.zfill(2) + ":" + s.zfill(2)
    
def solution(play_time, adv_time, logs):
    # 초 단위로 변경 
    play_time = time_cal(play_time)
    adv_time = time_cal(adv_time)
    
    result = [0] * (play_time+1)
    
    # 해당 시각에 시청 중인 사람 수 기록 
    for log in logs:
        start, end = log.split("-")
        start =  time_cal(start)
        end = time_cal(end)
        result[start] +=1 
        result[end] -=1 
        
    # 구간 별 시청자 수 표시 
    for i in range(1, len(result)):
        result[i] = result[i-1] + result[i]
        
    # 누적 시청자 수 표시 
    for i in range(1,len(result)):
        result[i] = result[i-1] + result[i]
    
    # 최대 시청자 수 저장 : 0초부터 광고를 시작하는 경우로 초기화 
    view = result[adv_time-1]
    answer = 0 
    
    for i in range(adv_time-1, play_time):
        # 구간 별 시청자 수 최댓값으로 갱신 
        if view < result[i] - result[i-adv_time]:
            view = result[i] - result[i-adv_time]
            answer = i - adv_time + 1 

    return str_cal(answer)
    
p = "02:03:55"
a = "00:14:15"
l = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(p,a,l))