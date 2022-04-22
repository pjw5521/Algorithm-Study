def solution(number, k):
    lim = len(number)-k
    num = ''

    for i in range(len(number)):
        t = number[i]
        if len(num) == lim:
            max = 0
            for i in range(len(num)):
                #z = num[0:i] + num[i+1:] + str(t) # 여기가 문제임 스트링을 계속 생성 중이니까
                if int(num[0:i] + num[i+1:] + str(t)) > max:
                    max = num[0:i] + num[i+1:] + str(t)
            num = str(max)
            continue
        num += number[i]
    return num

number = "4177252841"
print(solution(number,4))
#print(int(number[0:2]+number[3:]+str(4)))

#print(number[0:0]+number[1:])