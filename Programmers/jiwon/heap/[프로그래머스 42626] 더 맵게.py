import heapq 
def solution(scoville, K):
    answer = 0
    
    q = []
    
    # 스코빌 지수를 우선 순위로 하는 최소 힙 구현 
    for i in scoville :
        heapq.heappush(i)

    while True :
        # 가장 맵지 않은 음식의 스코빌 지수 
        h = heapq.heappop(q)
        
        # 가장 낮은 스코빌 지수가 K 이상이면 모든 음식의 스코빌 지수가 K 이상 
        if q >= K :
            return answer 
        
        # 섞을 음식이 남아있다면 
        if q:
            # 두번 째로 맵지 않은 음식의 스코빌 지수 * 2 한 값 더하기 
            h += (heapq.heappop(q) * 2)
            # 섞은 음식의 스코빌 지수 힙에 삽입 
            heapq.heappush(q)
        # 섞을 음식이 없다면 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없다는 뜻 
        else :
            break
    
    return -1 