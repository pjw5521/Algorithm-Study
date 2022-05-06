from collections import defaultdict


def solution(gems):
    size = len(set(gems))
    dict = defaultdict(int)
    dict[gems[0]] = 1
    result = [0, len(gems) - 1]
    start, end = 0, 0

    while end < len(gems):
        if len(dict) == size:
            if end - start < result[1] - result[0]:
                result = [start, end]
            if dict[gems[start]] == 1:
                del dict[gems[start]]
            else:
                dict[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            if gems[end] in dict.keys():
                dict[gems[end]] += 1
            else:
                dict[gems[end]] = 1
    return [result[0] + 1, result[1] + 1]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))