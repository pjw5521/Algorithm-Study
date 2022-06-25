# https://www.acmicpc.net/problem/14500
dx = [ 1, -1, 0, 0 ]
dy = [ 0, 0, 1, -1 ]

def dfs(x, y, result, cnt):
  global answer
  
  # 정사각형 4칸일 때 
  if cnt == 4:
    # 최댓값 갱신 
    answer = max(answer,result)
  if result + (4-cnt) * max_num < answer:
    return 
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<= nx < n and 0<= ny < m and not visited[nx][ny]:
      visited[nx][ny]= True
      # "ㅜ" 모양 탐색 
      if cnt== 2 :
        dfs(x, y, result+ graph[nx][ny], cnt + 1 )
      dfs(nx, ny, result+ graph[nx][ny] , cnt + 1)
      visited[nx][ny]= False
  
  return

n, m = map(int,input().split())

graph = []

visited = [ [False] * m for _ in range(n) ]

answer = 0 

for _ in range(n):
  graph.append(list(map(int,input().split())))

# 최댓값 저장 
max_num = max(map(max,graph))

for i in range(n):
  for j in range(m):
    visited[i][j] = True
    # 현재 위치, 결과의 합, 칸 수 
    dfs(i,j,graph[i][j], 1)
    visited[i][j] = False

print(answer)