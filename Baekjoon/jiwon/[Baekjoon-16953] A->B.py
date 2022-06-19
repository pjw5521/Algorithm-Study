# https://www.acmicpc.net/problem/16953
from collections import deque

def bfs(a,b):
    q = deque()

    q.append((a,0))
    
    while q :
        num, cnt = q.popleft()
        
        if num == b:
            # 최솟값에 1더한 값 리턴 
            return cnt + 1
        
        if num*2 <= b :
            # 2 곱한 값 추가 
            q.append((num*2, cnt+1))
            
        # 오른쪽에 1추가 
        tmp = str(num) + '1'
        tmp = int(tmp)
        
        if tmp <= b :
            q.append((tmp,cnt+1))         
            
    return -1   

a, b = map(int, input().split())
print(bfs(a,b))