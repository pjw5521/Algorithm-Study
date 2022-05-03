# https://programmers.co.kr/learn/courses/30/lessons/86053

# 파라메트릭 서치 
def solution(a, b, g, s, w, t):
    answer = int(1e9)
    
    start = 0 
    end =  int(1e9)
    
    while start <= end :
        mid = (start+end) // 2 
        total_gold = 0 
        total_silver = 0 
        total = 0 
        
        # 각 도시별 
        for i in range(len(g)):
            # 트럭 이동 횟수 
            cnt = (mid// (t[i] * 2) )
            
            # 편도로 한 번 더 이동 가능하면 
            if mid % (t[i] * 2 ) >= t[i]:
                cnt += 1 
                
            # 도시에서 가져올 수 있는 금의 양
            gold = 0
            # 도시에서 가져올 수 있는 은의 양 
            silver = 0 
            
            # 옮길 수 있는 최대 금
            if g[i] > w[i] * cnt :
                gold = w[i] * cnt 
            else:
                gold = g[i]
            
            # 옮길 수 있는 최대 은 
            if s[i] > w[i] * cnt :
                silver = w[i] * cnt
            else:
                silver = s[i] 
                
            # 옮길 수 있는 광물의 총합의 최댓값 더하기
            if w[i] * cnt <= s[i] + g[i]:
                total += w[i] * cnt 
            else:
                total += s[i] + g[i]
                
            # 옮길 수 있는 금과 은 더하기 
            total_gold += gold
            total_silver += silver 
                
        # 옮길 수 있는 최대 금의 개수가 옮겨야하는 금의 개수보다 크면 
        # 옮길 수 있는 최대 은의 개수가 옮겨야하는 은의 개수보다 크면 
        # 옮길 수 있는 최대 광물의 개수가 옮겨야하는 광물의 개수보다 크면   
        if total_gold >= a and total_silver >= b and total >= a+b:
            # 최소 시간 갱신 
            answer = min(answer,mid)
            end = mid -1 
        else:
            start = mid +1 
            
    return answer
    
a = 10
b= 10
g = [100]
s = [100]
w = [7]
t = [10]
print(solution(a,b,g,s,w,t))