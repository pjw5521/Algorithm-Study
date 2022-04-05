def solution(jobs):
    answer = 0
    n = len(jobs)
    # 소요 시간 순으로 정렬
    jobs.sort(key = lambda x : x[1])
    # 현재 시간 
    t = 0
    
    while jobs :
        for i in range(len(jobs)) :
            # 요청 시간이 현재 시간보다 작거나 같으면 실행 
            if jobs[i][0] <= t :
                # 대기시간 + 실행 시간 
                answer += t - jobs[i][0] + jobs[i][1]
                # 현재 시간 갱신 
                t += jobs[i][1]
                # 요청 제거 
                jobs.pop(i)
                break 
            # 현재 시점에 실행할 수 있는 요청이 없다면 시간 + 1 
            if i == len(jobs) - 1 :
                t += 1 
        
    return answer // n