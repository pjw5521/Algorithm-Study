def solution(people, limit):
    answer = 0
    cnt = 0
    people.sort()
    for i in people:
        print(answer,i,cnt)
        if i+answer <= 100:
            answer +=i
        else:
            answer = i
            cnt+=1
    return cnt+1

people=[70, 50, 80, 50]
limit = 100
print(solution(people,limit))