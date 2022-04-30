def solution(routes):
    # 차량 도착 위치 기준으로 정렬
    routes = sorted(routes, key = lambda x:x[1])
    # 처음 카메라 위치 저장, 카메라 설치 개수 + 1
    camera = routes[0][1]
    answer = 1
    for i in range(1, len(routes)):
        # 카메라가 차량 이동 경로에 있으면, 다음 차량으로 넘어감
        if camera in range(routes[i][0], routes[i][1] + 1):
            continue
        # 없으면 카메라 설치 개수 +1
        else:
            answer += 1
            # 차량 도착 위치에 카메라 설치
            camera = routes[i][1]

    return answer