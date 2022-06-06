def check(ans):
    for x, y, what in ans:
        # 기둥
        # 1. 바닥 위에
        # 2. 보의 한쪽 끝 부분 위
        # 3. 다른 기둥 위
        if what == 0:
            if y == 0 or [x-1, y, 1] in ans or [x, y, 1] in ans or [x, y-1, 0] in ans:
                continue
            else:
                return False
        # 보
        # 1. 한쪽 끝 부분이 기둥 위
        # 2. 양쪽 끝 부분이 다른 보와 동시에 연결
        elif what == 1:
            if [x, y-1, 0] in ans or [x+1, y-1, 0] in ans or ([x-1, y, 1] in ans and [x+1, y, 1] in ans):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []

    for f in build_frame:
        x, y, what, how = f

        if how == 1:  # 설치
            answer.append([x, y, what])
            if check(answer) is False:
                answer.remove([x, y, what])
        else:  # 삭제
            answer.remove([x, y, what])
            if check(answer) is False:
                answer.append([x, y, what])

    answer.sort()
    return answer

n1 = 5
build_frame1 = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

n2 = 5

build_frame2 = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n1,build_frame1))

print(solution(n2,build_frame2))


