# https://programmers.co.kr/learn/courses/30/lessons/67258
from collections import defaultdict 

def solution(gems):
    answer = []
    
    # 서로 다른 보석의 개수 
    num = len(set(gems))
    # 보석의 개수 저장할 딕셔너리 
    dic = defaultdict(int)
    start, end = 0,0 
    # 구간 길이 
    cnt = len(gems) +1 
    
    while end < len(gems):
    	# 구간에 있는 보석 개수 증가 
        dic[gems[end]] += 1 
        end += 1 
        
        # 보석이 다 존재한다면 
        if len(dic) == num :
            
            while start < end :
                # 뒤에 하나 더 있다는 뜻이므로 start + 1 
                if dic[gems[start]] > 1 :
                    dic[gems[start]] -= 1
                    start += 1 
                # 구간 범위 최소로 갱신 
                elif end - start < cnt :
                    cnt = end - start 
                    answer = [start+1, end]
                    break
                # 그대로면 중단 
                else:
                    break 

    return answer 

g = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(g))