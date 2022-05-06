
# 실패한 코드 효율성이 있기 때문에 인덱싱으로 풀면 안된다.
# 잦은 검색이 필요한 경우에는 dict을 이용해야한다. - 검색에 해싱이 사용되기 때문에
'''
실패코드1
x = set(a)
start_i, end_i = 0,1
min_len = len(a)
while True:
    if(start_i == len(a)):
        break;
    l = end_i - start_i
    y = set(a[start_i:end_i])
    print(start_i,end_i,y,min_len)
    if(x == y):
        if(min_len<len(y)):
            min_len = y
            start_i +=1
            end_i = start_i+1
        else:
            continue
    else:
        if(end_i == len(a)-1):
            start_i+=1
            end_i = start_i+1
        else:
            end_i+=1
def solution(gems):
    N = len(gems)
    answer = [0, N - 1]
    kind = len(set(gems))  # 보석종류
    dic = {gems[0]: 1, }  # 종류 체크할 딕셔너리
    s, e = 0, 0  # 투포인터
    while s < N and e < N:
        print("b",dic, s, e)
        if len(dic) < kind:  # 종류 부족하면 end point 증가 & dic 개수 증가
            e += 1
            if e == N:
                break
            dic[gems[e]] = dic.get(gems[e], 0) + 1

        else:  # 종류 같으면 ans 비교 후 답 갱신하고, start point 증가 & dic 개수 다운
            if (e - s + 1) < (answer[1] - answer[0] + 1):
                answer = [s, e]
            if dic[gems[s]] == 1:
                del dic[gems[s]]
            else:
                dic[gems[s]] -= 1
            s += 1
        print("a",dic, s, e,answer)

    answer[0] += 1
    answer[1] += 1
    return answer

print(solution(a))
'''


a = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
b = ["AA", "AB", "AC", "AA", "AC"]
c = ["XYZ", "XYZ", "XYZ"]
d = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

# 실패코드 2
def solution(gems):
    answer = []
    start_i,end_i = 0,0
    j_kind = len(set(gems))
    j_count = {gems[0]:1,}
    print(j_kind)
    while True:
        print(j_count,start_i,end_i)
        if len(j_count) < j_kind:
            end_i+=1
            if end_i == len(gems):
                break
            j_count[gems[end_i]] = j_count.get(gems[end_i],0) + 1
            # 여기서 0을 넣는 이유는?
        else: # 우선 보석 카운팅은 다 된거
            #j_count[gems[start_i]] 여기서 value 값이 1초과면 value를 줄이고 value가 1이면 그냥 Return
            #print("보석갯수",gems[start_i],j_count[gems[start_i]])
            if(j_count[gems[start_i]] > 1):
                j_count[gems[start_i]] -= 1
            else:
                answer.append(start_i+1)
                answer.append(end_i+1)
                return answer
            start_i += 1
    return answer

def solution2(gems):
    answer = [0,len(gems)]
    start_i,end_i = 0,0
    j_kind = len(set(gems))
    j_count = {gems[0]:1,}
    print(j_kind)
    while start_i<len(gems) and end_i<len(gems):
        print(j_count,start_i,end_i)
        if len(j_count) < j_kind:
            end_i+=1
            if end_i == len(gems):
                break
            j_count[gems[end_i]] = j_count.get(gems[end_i],0) + 1
            # 여기서 0을 넣는 이유는?
        else: # 우선 보석 카운팅은 다 된거
            #j_count[gems[start_i]] 여기서 value 값이 1초과면 value를 줄이고 value가 1이면 그냥 Return
            #print("보석갯수",gems[start_i],j_count[gems[start_i]])
            if (end_i-start_i+1) < (answer[1]-answer[0]+1):
                answer= [start_i,end_i]
            if j_count[gems[start_i]] ==1:
                del j_count[gems[start_i]]
            else:
                j_count[gems[start_i]]-=1
            start_i += 1
    answer[0]+=1
    answer[1]+=1
    return answer

#print(solution(a))

x = ["a","a","a","b","b"] #34
y =["a"] #11
z =["a","b","b","b","b","b","b","c","b","a"] #810
print(solution2(z))



