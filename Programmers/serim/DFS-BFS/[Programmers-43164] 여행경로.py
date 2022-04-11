from collections import defaultdict

def solution(tickets):
    answer = []
    dict = defaultdict()

    for i in tickets:
        if i[0] in dict:
            dict[i[0]].append(i[1])
        else:
            dict[i[0]] = [i[1]]

    for i in dict.keys():
        dict[i].sort(reverse=True)

    start = ["ICN"]

    while start:
        target = start[-1]
        if target not in dict or len(dict[target]) == 0:
            answer.append(start.pop())
        else:
            start.append(dict[target].pop())

    return answer[::-1]