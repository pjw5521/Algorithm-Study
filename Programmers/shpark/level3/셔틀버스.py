# n : 셔틀 운행 횟수, t : 셔틀 운행 간격, m : 한 셔틀에 탈 수 있는 최대 크루 수
def solution(n, t, m, timetable):
    answer = ''

    for i in range(len(timetable)):
        timetable[i] = int(timetable[i][0:2]) * 60 + int(timetable[i][3:])
    timetable.sort()

    busTime = []
    for i in range(n):
        busTime.append((9 * 60) + (t * i))

    i = 0
    for time in busTime:
        cnt = 0
        # 버스에 자리가 남음, 탑승할 크루가 남음, 해당 크루가 버스 도착 시간 전에 도착
        while cnt < m and i < len(timetable) and timetable[i] <= time:
            i += 1
            cnt += 1
        # 버스에 자리가 남는 경우 -> 콘은 버스 도착시간에 도착
        if cnt < m:
            answer = time
        # 버스에 자리가 없는 경우 -> 맨 마지막 버스 크루보다 1분 먼저 도착
        else:
            answer = timetable[i-1] - 1

    answer = str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)
    return answer