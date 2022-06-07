# https://programmers.co.kr/learn/courses/30/lessons/42892

# 전위 순회 
def preorder(nodes, answer):
    # 중심이 될 루트 노드 
    node = nodes[0]
    # 왼쪽 트리 노드 
    left = []
    # 오른쪽 트리 노드 
    right = []
    
    for i in range(1,len(nodes)):
        # x 좌표 값 비교 
        # 작으면 왼쪽에 위치 
        if node[0] > nodes[i][0]:
            left.append(nodes[i])
        # 크면 오른쪽에 위치 
        else :
            right.append(nodes[i])
    
    # 전위 순회이므로 노드 번호 먼저 추가 
    answer.append(node[2])
    
    if len(left) > 0 :
        preorder(left,answer)
    if len(right) > 0 :
        preorder(right,answer)
        
    return 
    
def postorder(nodes, answer):
    # 중심이 될 루트 노드 
    node = nodes[0]
    
    # 왼쪽 트리 노드 
    left = []
    # 오른쪽 트리 노드 
    right = []
    
    for i in range(1,len(nodes)):
        # x 좌표 값 비교
        # 작으면 왼쪽에 위치 
        if node[0] > nodes[i][0]:
            left.append(nodes[i])
        # 크면 오른쪽에 위치 
        else:
            right.append(nodes[i])

    if len(left) > 0 :
        postorder(left,answer)
    if len(right) > 0 :
        postorder(right,answer)
    
    # 후위 순회이므로 제일 마지막에 노드 번호 추가 
    answer.append(node[2])
    
    return 
    
def solution(nodeinfo):
    nodes = []
    
    # 노드 위치, 노드 번호 추가 
    for i in range(len(nodeinfo)):
        # [x좌표, y좌표, 노드 번호]
        nodes.append((nodeinfo[i][0], nodeinfo[i][1], i+1))
        
    # y좌표 기준 내림차순, x좌표 기준 오름차순 정렬
    nodes.sort(key = lambda x : (-x[1],x[0]))
    
    # 전위 순회 결과 저장 
    preanswer = []
    # 후위 순회 결과 저장
    postanswer = []
    
    preorder(nodes,preanswer)
    postorder(nodes,postanswer)
    
    return [preanswer, postanswer]
    
n = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(n))