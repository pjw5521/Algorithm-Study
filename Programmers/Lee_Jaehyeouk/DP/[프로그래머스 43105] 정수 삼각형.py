def solution(triangle):
    answer = 0
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution(triangle))


def self_solution(triangle):
    if len(triangle) == 1:
        return triangle


    return self_solution(triangle)

