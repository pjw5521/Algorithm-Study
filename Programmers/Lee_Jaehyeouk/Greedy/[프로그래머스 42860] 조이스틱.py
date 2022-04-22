def solution(name):

    value = [min(ord(i) - ord('A'), ord('Z')-ord(i)+1) for i in name]
    step = 0
    answer = 0
    print(value)
    while True:
        answer += value[step]
        value[step] = 0

        if sum(value) == 0:
            return answer

        left,right = 1,1

        while value[step-left] == 0:
            left += 1
        while value[step+right] == 0:
            right += 1
        if left >= right:
            step += right
            answer += right
        else:
            step -= left
            answer += left
        print(step,answer)

    return answer


name = "JAROBAT"
name1 = "JTAZDA"
name2 = "JAN"


print(solution(name))


def solution2(name):

    value = [min(ord(i) - ord('A'), ord('Z')-ord(i)+1) for i in name]
    step = 0
    answer = 0
    print(value)
    while True:
        answer += value[step]
        value[step] = 0

        if sum(value) == 0:
            return answer

        left,right = 1,1
        left_side, right_side = 0,0

        while value[step-left] == 0:
            left_side += value[step-left]
            left += 1
        while value[step+right] == 0:
            right_side += value[step+right]
            right += 1
        if left >= right:
            step -= left
            answer += left_side
        else:
            step += right
            answer += right_side
        print(step,answer)

    return answer
