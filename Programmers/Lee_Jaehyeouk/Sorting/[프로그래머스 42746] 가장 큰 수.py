def solution(numbers):
    t = []
    cnt = 0
    answer = ''
    for i in numbers:
        if len(str(i)) == 1:
            i = str(i)*6
        elif len(str(i)) == 2:
            i = str(i)*3
        elif len(str(i)) == 3:
            i = str(i)*2
        else:
            i = '100'
        t.append([str(i),cnt])
        cnt = cnt+1
    t.sort(reverse = True)
    for i in range(len(t)):
        answer = answer + str(numbers[t[i][1]])

    return str(int(answer))




