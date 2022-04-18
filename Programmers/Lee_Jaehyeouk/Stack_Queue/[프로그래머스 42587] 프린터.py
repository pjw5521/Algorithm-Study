def solution(priorities, location):
    ml = [0 for x in priorities]
    ml[location] = 1
    index = 0
    count = 1
    while True:
        t = priorities[0]
        s = ml[0]
        cnt = 0
        for i in priorities:
            if i > t:
                cnt += 1
        if cnt > 0:
            del priorities[0]
            del ml[0]
            priorities.append(t)
            ml.append(s)
        else:
            if ml[0] == 1:
                return count
            else:
                count +=1
                del priorities[0]
                del ml[0]
    answer = 0
    return answer