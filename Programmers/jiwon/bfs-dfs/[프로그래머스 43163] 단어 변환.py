from collections import deque, defaultdict

def bfs(word, target, words):
    
    # 방문 체크할 딕셔너리 
    visited = defaultdict(bool)
    
    q = deque()
    # 단어와 변환 횟수 
    q.append((word, 0))
    
    while q :
        w, cnt = q.popleft()
        
        # 타켓 단어이면 변환 횟수 리턴 
        if w == target :
            return cnt 
            
        # 단어 리스트에 있는 모든 단어들에 대하여 
        for s in words :
            # 방문하지 않았으면 
            if not visited[s] :
                # 다른 알파벳의 개수 
                num = 0 
                
                for i in range(len(s)):
                    if s[i] != w[i]:
                        num += 1 
                    if num > 1 :
                        break 
                
                # 하나만 다르면 큐에 삽입 
                if num == 1 :
                    q.append((s, cnt +1 ))
                    visited[s] = True
                    
    return 0
    
def solution(begin, target, words):

    # words에 타겟 단어가 없으면 변환할 수 없음 
    if target not in words :
        return 0    
    
    return bfs(begin, target, words)