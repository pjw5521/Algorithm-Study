from collections import deque

def solution(n, k, cmd):
    # 삭제된 인덱스 번호 저장 
    q = deque()
    # 인덱스 별 상태 저장 
    answer = ['O'] * n
    # 인덱스 별 가리키고 있는 이전 노드, 다음 노드 번호 저장 
    connect = []
    
    for i in range(n-1):
        connect.append([i-1, i+1])
        
    # 맨 앞, 맨 뒤 일 경우 -1 가리키고 있게 함 
    connect.append([n-2,-1])
    
    for s in cmd :
        s = s.split()
        
        # X칸 아래 
        if s[0] == 'D':
            for _ in range(int(s[1])):
                k = connect[k][1]
                
        # X칸 위 
        if s[0] == 'U':
            for _ in range(int(s[1])):
                k = connect[k][0]
                
        # 현재 행 삭제 
        if s[0] == 'C':
            # 삭제 상태로 변경 
            answer[k] = 'X'
            # 큐에 삭제 인덱스 번호 저장 
            q.append(k)
            
            pre = connect[k][0]
            next = connect[k][1]
            # 가장 마지막 꺼 삭제 
            if next == -1 :
                connect[pre][1] = -1 
                k = pre
            # 가장 앞에꺼 삭제 
            elif pre == -1 :
                connect[next][0] = pre
                k = next 
            else :
                connect[pre][1] = next 
                connect[next][0] = pre
                k = next 

        # 가장 최근에 삭제된 행 원래대로 복구 
        if s[0] == 'Z':
            num = q.pop()
            answer[num] = 'O'
            pre = connect[num][0]
            next = connect[num][1]
            
            # 가장 뒤에꺼 복구 
            if next == -1 :
                connect[pre][1] = num
            # 가장 앞에꺼 복구 
            elif pre == -1 :
                connect[next][0] = num
            # 사이에 있는 거 복구 
            else :
                connect[next][0] = num
                connect[pre][1] = num
                
            
    return "".join(answer)

n = 8
k = 2
cmd =["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n,k,cmd))