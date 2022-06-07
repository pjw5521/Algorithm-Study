# https://programmers.co.kr/learn/courses/30/lessons/60061
def solution(n, build_frame):
    answer = []
    
    # 기둥 연결 표시 
    build_col = [ [0] * (n+1) for _ in range(n+1) ]
    # 보 연결 표시 
    build_row = [ [0] * (n+1) for _ in range(n+1) ]
    
    for x, y, a , b in build_frame:
        
        # 설치 
        if b == 1 :
            # 기둥 
            if a == 0 :
                # 바닥에 있을 때 
                if y == 0 :
                    # 기둥 세우기 
                    build_col[x][y] = 1 
                    answer.append([x,y,a]) 
                else :
                    # 보나 기둥 위에 있을 때 
                    if build_col[x][y-1] or build_row[x-1][y] or build_row[x][y]:
                        # 기둥 세우기 
                        build_col[x][y] = 1 
                        answer.append([x,y,a]) 
            # 보 
            if a == 1 :
                # 한 쪽 끝 부분이 기둥 위, 양쪽 끝부분이 다른 보와 동시에 연결 
                if build_col[x][y-1] or build_col[x+1][y-1] or (build_row[x-1][y] and build_row[x+1][y]):
                    # 보 연결 
                    build_row[x][y] = 1 
                    answer.append([x,y,a])
        # 삭제 
        else : 
            # 기둥 
            if a == 0 :
                # 위에 기둥 있으면 
                if build_col[x][y+1] == 1 :
                    # 보의 위에 있는 것이 아니면 
                    if build_row[x-1][y+1] == 0 and build_row[x][y+1] == 0 :
                        continue 
                
                # 오른쪽 위에 보가 있으면 
                if build_row[x][y+1] == 1 :
                    # 양쪽 끝 부분이 다른 보와 연결된 게 아니고, 다른 쪽이 기둥 위가 아니면 
                    if not (build_row[x-1][y+1] and build_row[x+1][y+1]) and not build_col[x+1][y] :
                        continue 
                    
                # 왼쪽 위에 보가 있으면 
                if build_row[x-1][y+1] == 1 :
                    # 양쪽 끝 부분이 다른 보와 연결된 게 아니고, 다른 쪽이 기둥 위가 아니면 
                    if not (build_row[x][y+1] and build_row[x-2][y+1]) and not build_col[x-1][y] :
                        continue 
            
                # 제거 
                answer.pop(answer.index([x,y,a]))
                build_col[x][y] = 0 
                
            # 보 
            if a == 1 :
                # 왼쪽 위에 기둥 
                if build_col[x][y] == 1 :
                    # 아래쪽에 기둥도 없고, 왼쪽에 보도 없다면 
                    if not build_col[x][y-1] and not build_row[x-1][y] :
                        continue 
                # 오른쪽 위에 기둥 
                if build_col[x+1][y] == 1 :
                    # 아래쪽에 기둥도 없고, 오른쪽에 보도 없다면 
                    if not build_col[x+1][y-1] and not build_row[x+1][y] :
                        continue 
                # 왼쪽에 보
                if build_row[x-1][y] == 1 :
                    # 양쪽 아래쪽에 기둥 없다면 
                    if not build_col[x-1][y-1] and not build_col[x][y-1] : 
                        continue 
                # 오른쪽에 보 
                if build_row[x+1][y] == 1 :
                    # 양쪽 아래쪽에 기둥 없다면 
                    if not build_col[x+1][y-1] and not build_col[x+2][y-1]:
                        continue 
                
                # 제거 
                answer.pop(answer.index([x,y,a]))
                build_row[x][y] = 0
                
    # x좌표, y좌표, 기둥과 보 순으로 오름차순 정렬 
    answer.sort(key = lambda x : (x[0], x[1], x[2]))
    return answer
    
n = 5
b =[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n,b))

