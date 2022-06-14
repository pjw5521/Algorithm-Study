def str2int(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:])

    return hour + minute + second


def int2str(time):
    hour = str(time // 3600).zfill(2)
    minute = str(time % 3600 // 60).zfill(2)
    second = str(time % 3600 % 60).zfill(2)

    return hour + ":" + minute + ":" + second


def solution(play_time, adv_time, logs):
    # 1 동영상 전체 재생시간을 초로 바꾼 길이만큼의 배열 만들기
    dp = [0] * (str2int(play_time) + 1)
    adv_time = str2int(adv_time)
    play_times = str2int(play_time)

    # 2 재생했던 구간 정보를 돌면서 시작점에 +1, 끝점에 -1
    for i in logs:
        temp = i.split('-')
        start = str2int(temp[0])
        end = str2int(temp[1])
        print(start,end)
        dp[start] += 1
        dp[end] -= 1

    # 3 부분합 - 특정 초에 시청되는 인원 파악
    for i in range(1, play_times):
        dp[i] = dp[i] + dp[i - 1]

    # 4 부분합 - 누적 시청자 파악
    for i in range(1, play_times):
        dp[i] = dp[i] + dp[i - 1]

    # 5 누적합으로 가장 많이 시청한 인원 찾기 - 광고시간으로 슬라이딩 윈도우
    most_view = 0
    max_time = 0
    cnt = 0
    cnt1 = 0
    for i in range(adv_time - 1, play_times):
        if i >= adv_time:
            if most_view < dp[i] - dp[i - adv_time]:
                most_view = dp[i] - dp[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < dp[i]:
                most_view = dp[i]
                max_time = i - adv_time + 1
    #print(cnt, cnt1)
    return int2str(max_time)


play_time1 = "02:03:55"
adv_time1 = "00:14:15"
logs1 = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

play_time2 = "99:59:59"
adv_time2 = "25:00:00"
logs2 = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]

print(solution(play_time2,adv_time2,logs2))

play_time3 = "50:00:00"
adv_time3 = "50:00:00"
logs3 = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

print(solution(play_time1,adv_time1,logs1))

print(solution(play_time3,adv_time3,logs3))






