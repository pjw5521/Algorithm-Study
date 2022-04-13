from collections import deque, defaultdict 

def bfs(start,ticket):
    path = []
    q = deque()
    q.append(start)
    
    while q :
        x = q[-1]
        # 알파벳 내림차순 정렬 
        ticket[x].sort(reverse = True)
        # 더이상 이동할 수 없으면 
        if not ticket[x] or len(ticket[x]) == 0 :
            # 큐에서 제거하고 경로에 추가 
            path.append(q.pop())
        # 이동할 수 있으면 
        else :
            # 티켓 사용 
            next = ticket[x].pop()
            # 큐에 도착지 삽입 
            q.append(next)
    
    # 경로 뒤집기 
    path.reverse()
    return path
        
def solution(tickets):
    # 티겟의 출발지를 key, 도착지 리스트를 value 
    ticket = defaultdict(list)
    
    for i in range(len(tickets)):
        ticket[tickets[i][0]].append(tickets[i][1])
    
    return bfs('ICN', ticket)

t = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(t))