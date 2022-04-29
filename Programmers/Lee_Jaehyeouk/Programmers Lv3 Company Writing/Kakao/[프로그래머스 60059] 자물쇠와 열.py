# 90도 회전 함수
def rotate_by_90deg(matrix):
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            new_matrix[j][n - 1 - i] = matrix[i][j]

    return new_matrix


# 3배x3배로 확장된 자물쇠의 가운데 부분 (original 자물쇠)이 모두 1인지 확인하는 체크 함수
def check(new_lock):
    n = len(new_lock) // 3

    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 3배 x 3배로 자물쇠 생성
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]


    # 중간 부분에 메인 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]

    # 키를 회전시키며 총 4번 검사 90,180,270,360
    for _ in range(4):
        key = rotate_by_90deg(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m): # 열쇠와 자물쇠 대조
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 검사 실시
                if check(new_lock):
                    return True

                # 맞지 않는다면 원복
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

#print(solution(key,lock))

