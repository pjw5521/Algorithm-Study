# https://programmers.co.kr/learn/courses/30/lessons/42860
def solution(name):
    answer = 0
    n = len(name)
    min_move = n 
    
    for i in range(len(name)) :
        # 위 또는 아래로 조작하여 알파벳 완성 최솟값 
        answer += min(abs(ord(name[i])-ord('A')), abs(ord('Z')- ord(name[i]) +1))
        next = i + 1 
        
        # 연속되는 A의 최대 길이 구하기 
        while next < n and name[next] == 'A':
            next += 1 
            
        # 일직선으로 가는 것, 연속되는 A의 왼쪽에서 시작에서 이동, 연속되는 A의 오른쪽에서 시작해서 이동하는 것의 최솟값 
        min_move= min(min_move, i + i + n - next, 2*(n-next) + i )  
    
    #  최소 좌우 이동거리 더하기 
    answer += min_move
            
    return answer 
    
n = "JAN"
print(solution(n))