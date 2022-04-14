def solution(money):
    noLast = [0 for _ in range(len(money))]
    yesLast = [0 for _ in range(len(money))]

    noLast[0] = noLast[1] = money[0]

    for i in range(2, len(money) - 1):
        noLast[i] = max(noLast[i - 1], noLast[i - 2] + money[i])

    yesLast[0] = 0
    yesLast[1] = money[1]

    for i in range(2, len(money)):
        yesLast[i] = max(yesLast[i - 1], yesLast[i - 2] + money[i])

    return max(max(noLast), max(yesLast))


print(solution([1, 2, 3, 1]))
