# https://programmers.co.kr/learn/courses/30/lessons/64064
from itertools import permutations 

# 제재 아이디가 될 수 있는지 확인 
def check(user,ban):
    
    for i in range(len(user)):
        # * 이면 넘어감 
        if ban[i] ==  '*':
            continue
        # 한글자라도 다르면 False 
        if user[i] != ban[i]:
            return False 
    
    return True 
    
def solution(user_id, banned_id):
    answer = []
    # 순열로 가능한 제재 아이디 구하기 
    permutes = list(permutations(user_id, len(banned_id)))
    
    for permute in permutes :
        cnt = 0 
        for i in range(len(banned_id)):
            user = permute[i]
            ban = banned_id[i]
            
            # 길이 다르면 실패 
            if len(user) != len(ban):
                break 
        
            if check(user,ban):
                cnt +=1 
            else:
                break
         
        # 제재 아이디 목록으로 가능하면 
        if cnt == len(banned_id):
            # 중복 제거를 위해 
            permute = set(permute)
            if permute not in answer:
                answer.append(permute)
             
    return len(answer)
    
u = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b = ["fr*d*", "*rodo", "******", "******"]
print(solution(u,b))