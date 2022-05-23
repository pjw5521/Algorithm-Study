# lock padding 넣기 M-1크기로
# 홈과 돌기가 맞는지 체크
# 90도씩 돌려서 체크

# key index저장
# lock N - M-1 ~ N + M-1 체크
# N크기 넘어가편 continue
# 홈 크기 찾아서 저장해서 홈이 다 맞으면 True

def run(N, M, index, lock, cnt):
    count = 0
    for x in range(-M + 1, N):
        for y in range(-M + 1, N):
            check = 0
            result = True
            for i, j in index:
                count += 1
                key_x = i + x
                key_y = j + y
                # lock 배열 크기 넘어감
                if key_x not in range(N) or key_y not in range(N):
                    continue
                # 홈이 맞을 때
                if lock[key_x][key_y] == 0:
                    check += 1
                if lock[key_x][key_y] == 1:
                    result = False
                    break

            # 자물쇠가 열리면
            if result == True:
                if cnt == check:
                    return True
            count = 0

    return False


def solution(key, lock):
    answer = False
    N = len(lock)
    M = len(key)
    index = []

    # key index 저장
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                index.append([i, j])

    if len(index) == 0:
        return False

    # lock 홈 개수 저장
    cnt = 0
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                cnt += 1

    answer = run(N, M, index, lock, cnt)
    if answer == True:
        return answer

    # 90도 회전
    for k in range(3):
        temp = []
        for x, y in index:
            if k == 0:
                n_x, n_y = y, (M - 1) - x
            elif k == 1:
                n_x, n_y = (M - 1) - x, (M - 1) - y
            elif k == 2:
                n_x, n_y = (M - 1) - y, x
            temp.append([n_x, n_y])

        answer = run(N, M, temp, lock, cnt)
        if answer == True:
            return answer

    return answer