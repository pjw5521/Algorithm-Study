# https://programmers.co.kr/learn/courses/30/lessons/42884
def solution(routes):
    answer = 1
    # 반드시 나가는 시간 기준으로 정렬해줘야 함 
    routes.sort(key = lambda x : x[1])
    # 가장 빨리 나가는 차량의 진출 지점에 설치 
    camera = routes[0][1]
    
    for i in range(1, len(routes)):
        # 차량의 진입 시점이 카메라와 만나지 않으면 
        if routes[i][0] > camera:
            # 차량의 진출 시점에 새로운 카메라 설치 
            camera = routes[i][1]
            # 카메라 수 + 1 
            answer += 1 
            
    return answer
    
r = [[-100,100],[50,170],[150,200],[-50,-10],[10,20],[30,40]]
print(solution(r))