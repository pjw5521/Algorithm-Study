# 문제 풀이

## **단어 변환**


### 문제링크
- https://programmers.co.kr/learn/courses/30/lessons/43163


### 풀이 방법 

- words에 타켓 단어가 없으면 변환할 수 없으므로 바로 0 리턴

1. 단어 이름을 value, 방문 여부를 value로 하는 visited 딕셔너리 선언 
2. 큐에 (단어이름, 단어변환횟수) 삽입 
3. 큐에 단어가 남아있을 때까지 반복 
- 단어 리스트에 있는 모든 단어들에 대하여, 방문하지 않았으면 다른 알파벳의 개수 체크
- 다른 알파벳의 개수가 1개라면 큐에 삽입, 단어 변환 횟수 + 1, 방문 표시 

</br>

## **여행 경로**


### 문제링크
- https://programmers.co.kr/learn/courses/30/lessons/43164


### 풀이 방법 

초기 코드 
1. defalutdict(list)에 출발지를 Key, 도착지 리스트 value로 저장 
2. 출발지마다 도착지 리스트를 정렬해준 후, 순서가 앞서는 것을 도착지로 설정 

두개의 테스트 코드를 통과하지 못함
- **주어진 항공권은 모두 사용해야 합니다.** 라는 조건을 만족시키지 않기 때문 
```python
# 틀린 코드 
from collections import deque, defaultdict 

def bfs(start,ticket):
    # 경로 저장
    path = []
    path.append(start)

    q = deque()
    q.append(start)
    
    while q :
        x = q.popleft()
        
        #  아직 남아있는 티켓이 있으면 
        if x in ticket and len(ticket[x]) != 0 :
            # 알파벳 내림차순 정렬 
            ticket[x].sort(reverse = True)
            # 알파벳 순서가 가장 빠른 도착지 
            next = ticket[x].pop()
            # 경로에 추가 
            path.append(next)
            q.append(next)

    return path
        
def solution(tickets):
    ticket = defaultdict(list)
    
    for i in range(len(tickets)):
        ticket[tickets[i][0]].append(tickets[i][1])
    
    return bfs('ICN', ticket)
```
해결 방법
- 스택에 갈 수 있는 위치를 쌓아 놓은 후, 더이상 갈 수 있는 위치가 없으면 되돌아 가는 방법으로 해결할 수 있었다. 

1. defalutdict(list)에 출발지를 Key, 도착지 리스트 value로 저장 
2. 큐의 마지막 원소를 확인
- 더이상 이동할 수 없으면 큐에서 제거하고, 경로에 추가 
- 이동할 티켓이 남아있다면 티켓 리스트에서 제거하고, 큐에 도착지 삽입 
3. 경로 뒤집기 