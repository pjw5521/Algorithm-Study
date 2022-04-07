def solution(array, commands):
    ans = []
    answer = []
    for i in commands:
        ans = array[i[0] - 1:i[1]]
        k = i[2]
        ans.sort()
        answer.append(ans[k-1])
    return answer