from collections import deque

def solution(n, computers):
    answer = 0 
    visited = [False] * (n)
    
    # 방문하지 않은 노드마다 bfs 수행 
    for i in range(n):
      if visited[i] == False :
        bfs(computers, i, visited, n)
        answer += 1 

    return answer

# bfs 
def bfs(computers, start, visited, n):
  q = deque()
  q.append(start)

  while q:
    x = q.popleft()
    visited[x] = True
    # 연결된 노드이면 방문 기록 후 큐에 추가 
    for i in range(n):
      if computers[x][i] == 1 and visited[i] == False:
        visited[i] = True
        q.append(i)