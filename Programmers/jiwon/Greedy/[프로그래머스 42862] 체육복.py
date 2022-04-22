# https://programmers.co.kr/learn/courses/30/lessons/42862
from collections import defaultdict 

def solution(n, lost, reserve):
    # 현재 체육 수업을 들 수 있는 학생 수 
    answer = n - len(lost)
    dict = defaultdict(int)
    # 정렬 안해주면 테케 통과 x 
    lost.sort()
    reserve.sort()
    
    # 체육복 있는 사람 1 
    for i in reserve :
        dict[i] = 1
        
    for i in lost:
        # 도난 당한 학생이 여벌 체육복이 있을 때 
        if dict[i] :
            # 체육복 개수 줄이고
            dict[i] = 0 
            # 들을 수 있는 학생 수 증가 
            answer += 1 
        else :
            # 체육복 없음 표시 
            dict[i] = -1 
            
    for i in lost:
        # 체육복 없으면 
        if dict[i] == -1 :
            # 앞 번호가 체육복 있으면 빌려줌 
            if dict[i-1] == 1 :
                dict[i-1] = 0
                dict[i] = 0 
                answer += 1 
            # 뒷 번호가 체육복 있으면 빌려줌 
            elif dict[i+1] == 1 :
                dict[i+1] = 0
                dict[i] = 0 
                answer += 1 
                
    return answer
    
n = 3
l = [1,2]
r  = [2,3]
print(solution(n,l,r))