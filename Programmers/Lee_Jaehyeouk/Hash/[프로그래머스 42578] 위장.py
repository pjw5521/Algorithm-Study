def solution(clothes):
    ct = {}
    answer = 1

    for cloth in clothes:
        if cloth[1] in ct.keys():
            ct[cloth[1]].append(cloth[0])
        else:
            ct[cloth[1]] = [cloth[0]]

    for value in ct.values():
        answer *= len(value) + 1

    return answer - 1