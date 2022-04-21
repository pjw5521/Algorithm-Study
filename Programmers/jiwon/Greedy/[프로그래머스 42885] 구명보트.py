# https://programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    answer = 0
    people.sort()
    start =0 
    end = len(people) -1 
    s = 0 
    
    while start <= end  :
		# 가장 큰 것과 가장 작은 것 둘 다 태울 수 있으면 
        if people[start] + people[end] <= limit :
        	# 둘 다 태움 
            start +=1 
            end -=1 
        # 아니면 큰 것만 태움 
        else :
            end -=1 
            
        answer += 1 
    
    return answer
    
p = [70, 80, 50]
l = 100
print(solution(p,l))