def solution(prices):
    answer = []
    st = []
    for i in range(len(prices)):
        point = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                point = point + 1
            else:
                point = point + 1
                break;
        answer.append(point)
    return answer
