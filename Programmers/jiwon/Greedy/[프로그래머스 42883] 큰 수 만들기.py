def solution(number, k):
    # 제거한 숫자의 개수 
    cnt = 0 
    # index 
    idx = 0 
    
    while True :
        # 현재 위치의 숫자가 다음 숫자보다 작으면 제거 
        if number[idx] < number[idx + 1]:
            number = number[:idx] + number[idx+1:]
            cnt += 1
            if idx != 0 :
                # 앞에서부터 다시 비교 
                idx -= 1 
        else :
            idx += 1 
            # 끝까지 비교했는데 다 앞 숫자가 크면 
            if idx == len(number) - 1 :
                # 맨 끝 숫자 제거 
                number = number[:-1]
                break 
            
        # 제거 다 했으면 
        if cnt == k :
            break 
        
    return number
    
n = "654321" 
k = 1
print(solution(n,k))