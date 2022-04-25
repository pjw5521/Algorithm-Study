# 90도 회전 
def rotate(key, m):
    tmp = [ [0] * m for _ in range(m) ]
    
    for i in range(m):
        for j in range(m):
            tmp[j][m-1-i] = key[i][j]
            
    return tmp
   
# 열 수 있는지 확인 
def check(board, n, m):
    for i in range(n):
        for j in range(n):
        	# 1이 아니면 
            if board[m+i][m+j] != 1 :
                return False 
                
    # 모두 1로 구성되어 있으면 
    return True 
    
def solution(key, lock):
    answer = True
    m = len(key)
    n = len(lock)
    
    # 자물쇠 늘리기 
    board = [ [0] * (m*2 + n) for _ in range(m*2+n)]
    
    # 가운데 자물쇠 놓기 
    for i in range(n):
        for j in range(n):
            board[m+i][m+j] = lock[i][j]
    
    rotate_key = key
    for _ in range(4):
    	# 회전시킨 key 
        rotate_key = rotate(rotate_key,m)
        
        # board의 각 위치에 대하여 
        for i in range(1,m+n):
            for j in range(1,m+n):
                
                # 열쇠 끼우기 
                for a in range(m):
                    for b in range(m):
                        if rotate_key[a][b] == 1 :
                            board[i+a][j+b] += 1 
                
                # 열릴 수 있는지 확인 
                if check(board, n, m):
                    return True 
                
                # 열쇠 제거 
                for a in range(m):
                    for b in range(m):
                        if rotate_key[a][b] == 1 :
                            board[i+a][j+b] -= 1 
        
    return False

k = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
l = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(k,l))