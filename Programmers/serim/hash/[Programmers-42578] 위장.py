def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[1] not in dic.keys():
            dic[i[1]] = 1
        else:
            dic[i[1]] += 1
    for i in dic.values():
        answer *= i + 1
    answer -= 1
    return answer
