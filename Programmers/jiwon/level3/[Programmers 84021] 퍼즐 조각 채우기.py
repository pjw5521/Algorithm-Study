 # https://programmers.co.kr/learn/courses/30/lessons/84021
from collections import deque 

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 90도 회전 
def rotate(board):
    n = len(board)
    m = len(board[0])
    tmp = [ [0] * n for _ in range(m) ]
    
    for i in range(n):
        for j in range(m):
            tmp[j][n-1-i] = board[i][j]
   
    return tmp
   
# 퍼즐 위치 구하기 
def find_puzzle(board, a, b, visited):
    puzzle = []
    visited[a][b] = True 
    n = len(board)
    
    q = deque()
    q.append((a,b))
    
    # bfs 
    while q :
        x, y = q.popleft()
        puzzle.append((x,y))
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True 
                q.append((nx,ny))
                
    return puzzle 
    
# 퍼즐 index 변경 
def trans_puz(puz):
	# 세로 최대, 최소 index 
    max_x, min_x = -1, int(1e9)
    # 가로 최대, 최소 index 
    max_y, min_y = -1, int(1e9)
    
    for i in range(len(puz)):
        x, y = puz[i]
        
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)
    
    # 세로 길이
    len_x = max_x - min_x + 1 
    # 가로 길이 
    len_y = max_y - min_y + 1 
    
    trans = [ [0] *len_y for _ in range(len_x)]
    
    for i in puz :
        x = i[0] - min_x
        y = i[1] - min_y
        trans[x][y] = 1 
        
    return trans

# 채워지는지 확인 
def check(puz, board):
    n = len(board)
    col = len(puz)
    row = len(puz[0])

    for i in range(n-col+1):
        for j in range(n-row+1):
            result = True
            
            for x in range(col):
                for y in range(row):
                	# 퍼즐 끼우기 
                    board[x+i][y+j] += puz[x][y]
                    # 채워질 수 없으면 
                    if board[i+x][j+y] != 1 :
                        result = False 
            
            # 내부 빈공간이 존재하면 
            if is_empty(board, puz, i, j):
                result = False 
                
            if result :
                return True 
            else:
            	# 퍼즐 제거 
                for x in range(col):
                    for y in range(row):
                        board[x+i][y+j] -= puz[x][y]
                    
    return False

# 빈공간 존재하는지 확인 
def is_empty(board,puz,i,j):
    n = len(board)
    col = len(puz)
    row = len(puz[0])
    
    for x in range(col):
        for y in range(row):
            if puz[x][y] == 1 :
                
                for z in range(4):
                    nx = x + dx[z] + i 
                    ny = y + dy[z] + j
                    
                    if 0<=nx <n and 0<=ny < n and board[nx][ny] != 1 :
                        return True
    return False 
    
def solution(game_board, table):
    answer = 0
    
    n = len(game_board)
    visited = [ [False] * n for _ in range(n) ]
    puzzle = []
    puz_sum = []
    
    # 퍼즐 모양 구하기 
    for i in range(n):
        for j in range(n):
            if table[i][j] and not visited[i][j]:
                tmp = find_puzzle(table, i, j, visited)
                puzzle.append(trans_puz(tmp))
                # 퍼즐로 채울 수 있는 개수 
                puz_sum.append(len(tmp))
               
    for i in range(len(puzzle)):
        p = puzzle[i]
        
        # 회전 
        for _ in range(4):
            p = rotate(p)
            
            if check(p, game_board):
                answer += puz_sum[i]
                break 
            
    return answer
    
g = [[0,0,0],[1,1,0],[1,1,1]]
t = [[1,1,1],[1,0,0],[0,0,0]]
print(solution(g,t))