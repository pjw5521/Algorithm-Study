def solution(progresses, speeds):
    answer = []
    while len(progresses) != 0:
        if progresses[0] >= 100:
            if len(progresses) == 1:
                answer.append(1)
                return answer
            else:
                cnt = 0
                for i in range(0,len(progresses)):
                    if progresses[i] >= 100:
                        cnt+=1
                    else:
                        break
                del progresses[0:cnt]
                del speeds[0:cnt]
                answer.append(cnt)
        else:
            for i in range(0,len(progresses)):
                progresses[i] = progresses[i] + speeds[i]
    return answer