def solution(citations):
    answer = len(citations)
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] < i + 1:
            answer = i
            break

    return answer