def solution(numbers, target):
    answer = [0]
    for i in numbers:
        tem = []
        for j in answer:
            tem.append(j+i)
            tem.append(j-i)
        answer = tem
        print(answer)
    cnt = 0
    for i in answer:
        if i == target:
            cnt += 1
    return cnt

numbers = [1,1,1,1,1]
target = 3

print(solution(numbers,target))